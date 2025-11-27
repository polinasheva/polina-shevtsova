import pygame
import math
import random 

pygame.init()
pygame.mixer.music.load('space_music.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE) 
pygame.display.set_caption("Солнечная система")
WIDTH, HEIGHT = 1000, 800
cx = WIDTH // 2
cy = HEIGHT // 2   
FPS = 60
clock = pygame.time.Clock()

class Planet:
    def __init__(self, screen, radius, orbit_radius, color=None, speed=0, angle=0, image_path=None):
        self.screen = screen
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.color = color
        self.speed = speed
        self.angle = angle
        self.x = 0
        self.y = 0
        self.image = None
        if image_path:
                self.image = pygame.image.load(image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (radius*2, radius*2))

    def update(self, dt):
        global cx, cy
        self.angle += self.speed * dt
        self.x = cx + self.orbit_radius * math.cos(self.angle)
        self.y = cy + self.orbit_radius * math.sin(self.angle)

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        else:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)
# Солнце
sun_radius = 40
sun_image = pygame.image.load("sun.png").convert_alpha()
sun_image = pygame.transform.scale(sun_image, (sun_radius*2, sun_radius*2))


# Переменные планет
mercury = Planet(screen, radius=8, orbit_radius=60, color=(100, 100, 100), speed=2.5, image_path="mercury.png")
venus   = Planet(screen, radius=12, orbit_radius=90, color=(200, 150, 50), speed=2.0, image_path="venus.png")
earth   = Planet(screen, radius=14, orbit_radius=130, color=(0, 0, 255), speed=1.5, image_path="earth.png")
mars    = Planet(screen, radius=10, orbit_radius=170, color=(255, 50, 0), speed=1.2, image_path="mars.png")
jupiter = Planet(screen, radius=25, orbit_radius=240, color=(200, 100, 0), speed=0.8, image_path="jupiter.png")
saturn  = Planet(screen, radius=22, orbit_radius=300, color=(200, 200, 100), speed=0.6, image_path="saturn.png")
uranus  = Planet(screen, radius=18, orbit_radius=350, color=(0, 200, 200), speed=0.4, image_path="uranus.png")
neptune = Planet(screen, radius=18, orbit_radius=400, color=(0, 0, 150), speed=0.3, image_path="neptune.png")

# Астероиды
asteroids = []
for i in range(100):
    angle_ast = random.uniform(0, 6.28)
    dist_ast = random.uniform(190, 210) 
    asteroids.append([angle_ast, dist_ast])
    
# Комета
comet_x = -100
comet_y = -100
comet_speed_x = 2
comet_speed_y = 1

# Луна
moon_angle = 0
moon_dist = 25
moon_speed = 5

running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            cx = WIDTH // 2
            cy = HEIGHT // 2
        
        # Если нажать мышкой, солнце переместится туда
        if event.type == pygame.MOUSEBUTTONDOWN:
            cx, cy = pygame.mouse.get_pos()

    # Обновляем планеты
    mercury.update(dt)
    venus.update(dt)
    earth.update(dt)
    mars.update(dt)
    jupiter.update(dt)
    saturn.update(dt)
    uranus.update(dt)
    neptune.update(dt)

    # Движение кометы
    comet_x += comet_speed_x
    comet_y += comet_speed_y
            
    # Если улетела, запускаем заново
    if comet_x > WIDTH + 100:
        comet_x = -100
        comet_y = random.randint(0, HEIGHT)
        
    screen.fill((0, 0, 20)) # Темный фон

    # Cолнце
    screen.blit(sun_image, (cx - sun_radius, cy - sun_radius))

    # Рисуем орбиты 
    pygame.draw.circle(screen, (50, 50, 50), (cx, cy), 130, 1) # Земля
    pygame.draw.circle(screen, (50, 50, 50), (cx, cy), 240, 1) # Юпитер

    # Рисуем астероиды
    for ast in asteroids:
        # Вращение
        ast[0] += 0.2 * dt
        ax = cx + ast[1] * math.cos(ast[0])
        ay = cy + ast[1] * math.sin(ast[0])
        pygame.draw.circle(screen, (150, 150, 150), (int(ax), int(ay)), 2)

    # Рисуем комету 
    pygame.draw.ellipse(screen, (200, 200, 255), (int(comet_x), int(comet_y), 20, 10))
   
    # Рисуем планеты
    mercury.draw()
    venus.draw()
    earth.draw()
    mars.draw()
    jupiter.draw()
    saturn.draw()
    uranus.draw()
    neptune.draw()

    # Вращение луны
    moon_angle += moon_speed * dt
    mx = earth.x + moon_dist * math.cos(moon_angle)
    my = earth.y + moon_dist * math.sin(moon_angle)
    pygame.draw.circle(screen, (200, 200, 200), (int(mx), int(my)), 4) # Луна - серый шарик

    pygame.display.flip()

pygame.quit()