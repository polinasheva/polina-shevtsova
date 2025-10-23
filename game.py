import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Падающие яйца")

spawn_points = [(50, 50), (150, 50), (250, 50), (350, 50)]

running = True
clock = pygame.time.Clock()

balls = []  
spawn_interval = 2000  
last_spawn_time = 0

key_sound = pygame.mixer.Sound("notification.wav")

background_game = pygame.image.load("nu_pogodi.jpg")
egg_image = pygame.image.load("egg.jpg").convert_alpha()
egg_image = pygame.transform.scale(egg_image, (40, 40))
chicken_image = pygame.image.load("chicken.png").convert_alpha()
chicken_image = pygame.transform.scale(chicken_image, (80, 80))
chicken_pos = (500, 200)
chick_image = pygame.image.load("chick.jpg").convert_alpha()
chick_image = pygame.transform.scale(chick_image, (80, 80))
chick_pos = (100, 200)
basket_image = pygame.image.load("basket.jpg").convert_alpha()
basket_image = pygame.transform.scale(basket_image, (80, 60))
basket_image.set_colorkey((255, 255, 255))
chicken_image.set_colorkey((255, 255, 255))
egg_image.set_colorkey((255, 255, 255))
chick_image.set_colorkey((255, 255, 255))

ball_data = [] 

basket_x = 300
basket_y = 250
step = 15

basket_radius = 30  
egg_radius = 20   

score = 0
missed_streak = 0
font = pygame.font.Font(None, 36) 

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and basket_y > 40: 
                basket_y -= step
            elif event.key == pygame.K_s and basket_y < 260:   
                basket_y += step
            elif event.key == pygame.K_a and basket_x > 40:    
                basket_x -= step
            elif event.key == pygame.K_d and basket_x < 560:   
                basket_x += step

    if current_time - last_spawn_time > spawn_interval:
        x, y = random.choice(spawn_points)
        angle = random.uniform(-45, 45)   
        balls.append([x, y])
        ball_data.append([x, y, angle])  
        last_spawn_time = current_time

    basket_rect = basket_image.get_rect(center=(basket_x, basket_y))
   
    for i in range(len(balls)):
        ball = balls[i]
        data = ball_data[i]
      
        angle_rad = math.radians(data[2])
        ball[0] += math.sin(angle_rad)  
        ball[1] += math.cos(angle_rad)  
       
        data[0] = ball[0]
        data[1] = ball[1]

        dx = basket_x - ball[0]
        dy = basket_y - ball[1]
        distance = (dx**2 + dy**2)**0.5
        if distance < basket_radius + egg_radius:
            key_sound.play() 
            score += 1
            balls[i] = None
            ball_data[i] = None
            missed_streak = 0  

    balls_to_keep = []
    ball_data_to_keep = []

    for i in range(len(balls)):
        if balls[i] is not None:
            if balls[i][1] < 400:
                balls_to_keep.append(balls[i])
                ball_data_to_keep.append(ball_data[i])
            else:
                missed_streak += 1
                if missed_streak >= 3:
                    print("Вы проиграли! (трижды пропустили)")
                    running = False
    
    balls = balls_to_keep
    ball_data = ball_data_to_keep

    screen.fill((255, 255, 255))
    screen.blit(background_game, (0, 0))  
    
    for ball in balls:
        egg_rect = egg_image.get_rect(center=(int(ball[0]), int(ball[1])))
        screen.blit(egg_image, egg_rect)

    chicken_rect = chicken_image.get_rect(center=chicken_pos)
    screen.blit(chicken_image, chicken_rect)

    chick_rect = chick_image.get_rect(center=chick_pos)
    screen.blit(chick_image, chick_rect)
    
    screen.blit(basket_image, basket_rect)
    
    score_text = font.render(f"Яйца: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()