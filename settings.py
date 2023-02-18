import pygame


class Settings:

    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.bg_image = pygame.image.load('images/space.jpg')

