import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Logs")

RED = (255, 0, 0)
WHITE = (255, 255, 255)

rect_width, rect_height = 200, 150
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(RED)

    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

pygame.quit()