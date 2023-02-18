import pygame


class Ship:
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализируем корабль и задаем его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship_4.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
