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
    ship = Ship(ai_setting, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


run_gam()
