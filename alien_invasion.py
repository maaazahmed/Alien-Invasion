# import pygame
# from setting import Settings
# from ship import Ship
# import functions as gf

# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Game")
#     ship = Ship(screen)
#     while True:
#         gf.check_events(ship)
#         gf.update_screen(ai_settings, screen, ship)


# run_game()


import pygame
import sys
from setting import Settings
import functions as gf
from ship import Ship 


def run_gam():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Gmae")
    ship = Ship(screen)

    while True:
        gf.check_events()
        gf.update_screen(ai_setting, screen, ship)
        
run_gam()
