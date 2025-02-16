import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bumbas animācija")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 40
ball_x = 0
ball_y = HEIGHT // 1.5
ball_speed = 10

running = True
while running:
    screen.fill(WHITE) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_speed
    if ball_x > WIDTH:
        ball_x = -ball_radius 

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip() 
    pygame.time.delay(30) 

pygame.quit()