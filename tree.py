import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

x, y = 250, 250
speed = 20
score = 0



coin_x = random.randint(0, 450)
coin_y = random.randint(0, 450)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()        
    if keys[pygame.K_a]: x -= speed
    if keys[pygame.K_d]: x += speed
    if keys[pygame.K_w]: y -= speed
    if keys[pygame.K_s]: y += speed


    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.fill((200, 200, 200))  # fons balts
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))
    screen.blit(text, (10, 10))

    if x < coin_x < x+50 and y < coin_y < y+50:
    # ja kvadrāts pieskaras monētai, ģenerē jaunu
     coin_x = random.randint(0, 450)
     coin_y = random.randint(0, 450)
     score += 1

    pygame.draw.circle(screen, (255, 255, 0), (coin_x, coin_y), 20)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
