import pygame
from setting import Settings


class Ship():
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/ship2.png")
        self.ract = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ract.centerx = self.screen_rect.centerx
        self.ract.bottom = self.screen_rect.bottom-5
        self.center = float(self.ract.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_setting.ship_speed_factor
        self.ract.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.ract)
