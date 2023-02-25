import pygame


class Settings:
    """Класс для хранения всех настроек игры Klissan Invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""

        self.screen_width = 1200
        self.screen_height = 800
        self.fullscreen_mode_on = False

        self.bg_image = pygame.image.load('images/space.jpg')
        self.icon_image = pygame.image.load('images/alien_ship.png')

        self.ship_speed = 7
        self.ship_limit = 4

        self.bullet_speed = 4
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 250, 60)
        self.bullet_allowed = 4
        self.bullet_not_god_mode = not False

        self.klissan_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
