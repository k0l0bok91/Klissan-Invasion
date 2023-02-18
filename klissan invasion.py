import sys
import pygame
from settings import Settings
from ship import Ship


class KlissanInvasion:
    """Класс для управления ресурсами игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Klissan Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и событий мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = KlissanInvasion()
    ai.run_game()
