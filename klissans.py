import pygame
from pygame.sprite import Sprite


class Klissan(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращаем True если пришелец достиг края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right == screen_rect.right or self.rect.left == 0:
            return True

    # def check_edges(self):
    #     """Возвращает True, если пришелец находится у края экрана."""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.bottom == screen_rect.bottom:
    #         return True
    #     elif self.rect.top == 0:
    #         return True

    def update(self, ai_game):
        """Перемещение пришельца"""
        self.x += (self.settings.klissan_speed * self.settings.fleet_direction)
        self.rect.x = self.x