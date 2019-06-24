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


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Alien Invasion")
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
run_game()