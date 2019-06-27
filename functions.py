# import pygame
# import sys


# def check_events(ship):
#     for event in pygame.event.get():
#         if event == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.rect.centerx += 10
#             elif event.key == pygame.K_LEFT:
#                 ship.rect.centerx -= 10
             

# def update_screen(ai_settings, screen, ship):
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#     pygame.display.flip()



import pygame 
import sys 
from setting import Settings

def check_events():
    for event in pygame.event.get():
        if event ==  pygame.QUIT:
            sys.exit()
            


def update_screen(ai_settings, screen, ship ):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()







   












