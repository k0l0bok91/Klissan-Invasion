import pygame
from pygame.sprite import Sprite
# from game_object import GameObject


class Bolts(Sprite):
    """Класс для управления снарядами, выпущенными кораблём"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bolt_color
        self.bolt = pygame.sprite.Group()
        self.rect = pygame.Rect(0, 0, self.settings.bolt_width, self.settings.bolt_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def moving_blaster_bolt_up(self):
        """Перемещает снаряд по экрану вверх"""
        self.y -= self.settings.bolt_speed
        self.rect.y = self.y

    def update_bolts(self):
        """Обновляет позицию снарядов и уничтожение страрых снарядов"""
        self.moving_blaster_bolt_up()

        for bolt in self.Sprite().Group().copy():
            if bolt.rect.bottom <= 0:
                self.bullets.remove(bolt)
        self._check_bolt_klissan_collision()

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _create_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bolts(self)
            self.bullets.add(new_bullet)
