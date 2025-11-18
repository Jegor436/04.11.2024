import pygame
import math

pygame.init()
ekrans = pygame.display.set_mode((600, 350))
pygame.display.set_caption('Latvijas svētku animācija')
clock = pygame.time.Clock()

font_static = pygame.font.Font(None, 40)
font_dynamic_size = 60
angle = 0

aplis_x = 50
aplis_y = 270
aplis_ātrums = 3

sarkans = (140, 0, 26)
balts = (255, 255, 255)

darbojas = True
while darbojas:
    for notikums in pygame.event.get():
        if notikums.type == pygame.QUIT:
            darbojas = False

    ekrans.fill((140, 0, 26))
    baltas_istelpa = 350 // 5
    pygame.draw.rect(ekrans, balts, (0, 140, 600, baltas_istelpa))

    teksts = font_static.render('Latvija 18. novembris', True, (255, 255, 255))
    ekrans.blit(teksts, (150, 20))

    angle += 0.05
    current_size = 50 + int(math.sin(angle) * 10)
    font_dynamic = pygame.font.Font(None, current_size)
    teksts_latvija = font_dynamic.render('Latvija', True, balts)
    ekrans.blit(teksts_latvija, (220, 90))

    aplis_x += aplis_ātrums
    if aplis_x > 580 or aplis_x <20:
        aplis_ātrums *= -1

    pygame.draw.circle(ekrans, balts, (aplis_x, aplis_y), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
