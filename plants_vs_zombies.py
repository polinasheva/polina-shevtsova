import pygame
import math
import random

pygame.init()

# Экран
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Plants vs. Zombies")

# Картинки
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (960, 540))

zombie_image_normal = pygame.image.load("zombies.png")
zombie_image_normal = pygame.transform.scale(zombie_image_normal, (80, 100))

zombie_image_strong = pygame.image.load("zombie2.png")
zombie_image_strong = pygame.transform.scale(zombie_image_strong, (80, 100))

shooter_image = pygame.image.load("plant.png")
shooter_image = pygame.transform.scale(shooter_image, (70, 70))

# Звуки
pygame.mixer.music.load("plants (3).mp3")
pygame.mixer.music.play(-1)
groan_sound = pygame.mixer.Sound("groan4.mp3")
zombie_falling_sound = pygame.mixer.Sound("zombie_falling_2.mp3")
fire_sound = pygame.mixer.Sound("firepea.mp3")

# Переменные для стрелка
shooter_x = 150
shooter_y = 445 
shooter_speed = 4

# Переменные для горошины (снаряда)
pea_x, pea_y = shooter_x, shooter_y
pea_radius = 10

# Физика
vx, vy = 0, 0
gravity = 0.2
power = 15
angle = 45
on_ground = True 

# Переменные для зомби
zombie_alive = False
zombie_health = 0
zombie_rect = pygame.Rect(0, 0, 0, 0)
current_zombie_image = None
zombie_spawn_counter = 0

# Скорость зомби
zombie_speed_x = 0
zombie_speed_y = 0


# Функция для создания нового зомби
def spawn_zombie(counter):
    # Позиция зомби
    zombie_x = random.randint(480, 960 - 80)
    zombie_y = random.randint(150, 480 - 100)
    
    # Выбор типа зомби
    if random.choice([True, False]):
        new_image = zombie_image_normal
        new_health = 1
    else:
        new_image = zombie_image_strong
        new_health = 3
        
    new_rect = new_image.get_rect(topleft=(zombie_x, zombie_y))
    new_alive = True
    
    # Задаем зомби скорость при появлении
    new_speed_x = 1
    new_speed_y = random.choice([-1, 1])

    # Звук появляется не каждый раз
    counter += 1
    if counter % 3 == 0:
        groan_sound.play()
    
    # Возвращаем все созданные значения
    return new_alive, new_health, new_rect, new_image, new_speed_x, new_speed_y, counter


# Текст
font = pygame.font.Font(None, 36)
score = 0

# Основной цикл игры
running = True
while running:
    if not zombie_alive:
        zombie_alive, zombie_health, zombie_rect, current_zombie_image, zombie_speed_x, zombie_speed_y, zombie_spawn_counter = spawn_zombie(zombie_spawn_counter)

    # Проверка всех событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                angle = min(angle + 5, 90)
            elif event.key == pygame.K_DOWN:
                angle = max(angle - 5, 10)
            elif event.key == pygame.K_RIGHT:
                power = min(power + 2, 30)
            elif event.key == pygame.K_LEFT:
                power = max(power - 2, 5)
            elif event.key == pygame.K_SPACE and on_ground:
                pea_x, pea_y = shooter_x, shooter_y 
                rad = math.radians(angle)
                vx = power * math.cos(rad)
                vy = -power * math.sin(rad)
                on_ground = False
                fire_sound.play()

    # Движение стрелка 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        shooter_x -= shooter_speed
    if keys[pygame.K_d]:
        shooter_x += shooter_speed
    if keys[pygame.K_w]:
        shooter_y -= shooter_speed
    if keys[pygame.K_s]:
        shooter_y += shooter_speed

    # Ограничения движения стрелка
    if shooter_x < 35: shooter_x = 35
    if shooter_x > 480: shooter_x = 480
    if shooter_y < 35: shooter_y = 35
    if shooter_y > 445: shooter_y = 445

    # Полет горошины
    if not on_ground:
        vy += gravity
        pea_x += vx
        pea_y += vy

    # Если горошина улетела
    if pea_y > 480 or pea_x > 960 or pea_x < 0:
        on_ground = True

    # Движение зомби, если он жив
    if zombie_alive:
        zombie_rect.x -= zombie_speed_x
        zombie_rect.y += zombie_speed_y

        if zombie_rect.top < 100 or zombie_rect.bottom > 480:
            zombie_speed_y = -zombie_speed_y

        if zombie_rect.left < 0:
            print("Игра окончена! Зомби победили.")
            running = False

    # Проверка попадания
    pea_rect = pygame.Rect(pea_x - pea_radius, pea_y - pea_radius, pea_radius * 2, pea_radius * 2)
    if zombie_alive and not on_ground and pea_rect.colliderect(zombie_rect):
        zombie_health -= 1
        on_ground = True
        
        if zombie_health <= 0:
            zombie_alive = False
            score += 1
            zombie_falling_sound.play()

    # Отрисовка всего на экране
    screen.blit(background, (0, 0))

    if on_ground:
        points = []
        rad = math.radians(angle)
        temp_vx = power * math.cos(rad)
        temp_vy = -power * math.sin(rad)
        temp_x, temp_y = shooter_x, shooter_y 
        for i in range(80): 
            temp_vy += gravity
            temp_x += temp_vx
            temp_y += temp_vy
            if temp_y > 480: break
            points.append((int(temp_x), int(temp_y)))
        if len(points) > 1:
            pygame.draw.lines(screen, (255, 255, 255, 100), False, points, 2)

    screen.blit(shooter_image, (shooter_x - 35, shooter_y - 35))

    if zombie_alive:
        screen.blit(current_zombie_image, zombie_rect)

    if not on_ground:
        pygame.draw.circle(screen, (50, 200, 50), (int(pea_x), int(pea_y)), pea_radius)
        pygame.draw.circle(screen, (30, 120, 30), (int(pea_x), int(pea_y)), pea_radius - 3)

    text_angle = font.render(f"Угол: {angle}°", True, (255, 255, 255))
    text_power = font.render(f"Сила: {power}", True, (255, 255, 255))
    text_score = font.render(f"Счёт: {score}", True, (255, 255, 0))
    screen.blit(text_angle, (10, 10))
    screen.blit(text_power, (10, 45))
    screen.blit(text_score, (960 - 120, 10))

    pygame.display.flip()
    pygame.time.delay(15)

pygame.quit()