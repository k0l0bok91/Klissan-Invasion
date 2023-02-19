import pygame


class Settings:
    """Класс для хранения всех настроек игры Klissan Invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('images/space.jpg')
        self.icon_image = pygame.image.load('images/ship_3.png')

        self.ship_speed = 1

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 200, 60)
