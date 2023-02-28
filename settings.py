import pygame


class Settings:
    """Класс для хранения всех настроек игры Klissan Invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Настройки разрешения
        self.screen_width = 1200
        self.screen_height = 800
        self.fullscreen_mode_on = False
        # Настройки окна
        self.bg_image = pygame.image.load('images/space.jpg')
        self.icon_image = pygame.image.load('images/alien_ship.png')
        # Настройки корабля
        self.ship_speed = 7
        self.ship_limit = 4
        # Настройки выстрела
        self.bolt_speed = 4
        self.bolt_width = 5
        self.bolt_height = 20
        self.bolt_color = (0, 255, 0)
        self.bolt_allowed = 4
        self.bolt_not_god_mode = not False

        self.klissan_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
