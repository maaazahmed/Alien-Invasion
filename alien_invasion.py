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


def run_gam():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Alien Gmae")

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        screen.fill((230, 230, 230))


# run_gam()
