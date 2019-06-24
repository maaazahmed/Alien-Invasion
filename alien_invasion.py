import pygame
import sys


# def run_game():
#     pygame.init()
#     pygame.display.set_mode((600, 600))
#     pygame.display.set_caption("Alien Invasion")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             pygame.display.flip()

# run_game()r


# >>>>>>>>>>>>>>>>>>>> Creating Game Window
# def run_game():
#     pygame.init()
#     screen = pygame.display.set_mode((900, 600))
#     pygame.display.set_caption("Alien Invasion")
#     while True:
#         for event in pygame.event.get():
#             if event == pygame.QUIT:
#                 sys.exit()
#         pygame.display.flip()
# run_game()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("git push -u origin master")
    screen.fill((230, 230, 230))
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()
