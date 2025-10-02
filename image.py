import pygame
import math

pygame.init()          
font = pygame.font.SysFont(None, 24)

screen = pygame.display.set_mode((900,600)) 
pygame.display.set_caption("картинка №1")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
     
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (161,245,255), (0,0,900,275)) #небо
    
    pygame.draw.rect(screen, (67,35,222), (0,275,900,150)) #море
    
    pygame.draw.rect(screen, (238,246,11), (0,425,900,225)) #песок
    
    pygame.draw.circle(screen, (255,247,30), (800,100), 45) #солнце
    
    pygame.draw.rect(screen, (228,129,27), (108,392,13,180)) #зонтик
    pygame.draw.polygon(screen, (242,77,73), [(114,360), (45,392), (182,392)]) 
    pygame.draw.aaline(screen, (205,66,63), (114,360), (165,392), 3)
    pygame.draw.aaline(screen, (205,66,63), (114,360), (144,392), 3)
    pygame.draw.aaline(screen, (205,66,63), (114,360), (122,392), 3)
    pygame.draw.aaline(screen, (205,66,63), (114,360), (99,392), 3)
    pygame.draw.aaline(screen, (205,66,63), (114,360), (73,392), 3)
    pygame.draw.aaline(screen, (205,66,63), (114,360), (55,392), 3)
    
    pygame.draw.rect(screen, (1,1,1), (615,163,10,160)) #мачта
    
    pygame.draw.polygon(screen, (222,214,152), [(625,163), (645,240), (715,240)]) #парус
    pygame.draw.polygon(screen, (0,0,0), [(625,163), (645,240), (715,240)], 1)
    pygame.draw.polygon(screen, (222,214,152), [(645,240), (715,240), (626,322)])
    pygame.draw.polygon(screen, (0,0,0), [(645,240), (715,240), (626,322)], 1)
    
    pygame.draw.rect(screen, (186,80,6), (500,322, 280,44)) #лодка
    pygame.draw.polygon(screen, (186,80,6), [(780,322), (847,322), (780,366)])
    pygame.draw.aaline(screen, (162,74,52), (780,322), (780,365), 2)
    pygame.draw.aaline(screen, (162,74,52), (500,322), (500,365), 2)
    
    pygame.draw.circle(screen, (255,255,255), (798,336), 10) #окошко
    pygame.draw.circle(screen, (0,0,0), (798,336), 10, 4)
    
    pygame.draw.circle(screen, (255,255,255), (150,65), 20) #облака
    pygame.draw.circle(screen, (217,231,234), (150,65), 20, 2)
    pygame.draw.circle(screen, (255,255,255), (126,78), 20)
    pygame.draw.circle(screen, (217,231,234), (126,78), 20, 2)
    pygame.draw.circle(screen, (255,255,255), (175,65), 20)
    pygame.draw.circle(screen, (217,231,234), (175,65), 20, 2)
    pygame.draw.circle(screen, (255,255,255), (152,82), 20)
    pygame.draw.circle(screen, (217,231,234), (152,82), 20, 2)
    pygame.draw.circle(screen, (255,255,255), (178,85), 20)
    pygame.draw.circle(screen, (217,231,234), (178,85), 20, 2)
    pygame.draw.circle(screen, (255,255,255), (201, 65), 20)
    pygame.draw.circle(screen, (217,231,234), (201,65), 20, 2)
    pygame.draw.circle(screen, (255,255,255), (207, 83), 20)
    pygame.draw.circle(screen, (217,231,234), (207, 83), 20, 2)
    pygame.draw.polygon(screen, (186,80,6), [(500,322), (500,366), (430,320)]) #часть лодки
    
    center_x, center_y = 489, 315 #арка для лодки
    radius = 44
    start_angle = math.pi/4  
    end_angle = 3*math.pi/4 
    width = 15
    segments = 100
    
    rotation_angle = math.pi/5
    inner_radius = radius - width / 2
    outer_radius = radius + width / 2
    
    points = []
    
    for i in range(segments + 1):
        angle = start_angle + (end_angle - start_angle) * i / segments
        rotated_angle = angle + rotation_angle  
        x = center_x + outer_radius * math.cos(rotated_angle)
        y = center_y + outer_radius * math.sin(rotated_angle)
        points.append((x, y))
    
    for i in range(segments, -1, -1):
        angle = start_angle + (end_angle - start_angle) * i / segments
        rotated_angle = angle + rotation_angle 
        x = center_x + inner_radius * math.cos(rotated_angle)
        y = center_y + inner_radius * math.sin(rotated_angle)
        points.append((x, y))
    
    pygame.draw.polygon(screen, (186,80,6), points)
    
    mx, my = pygame.mouse.get_pos()
    text = font.render(f"x: {mx}, y: {my}", True, (0, 0, 0))
    screen.blit(text, (10, 10))


    pygame.display.flip()
    

pygame.quit()
