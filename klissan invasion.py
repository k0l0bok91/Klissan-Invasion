import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from klissans import Klissan


class KlissanInvasion:
    """Класс для управления ресурсами игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Klissan Invasion")
        pygame.display.set_icon(self.settings.icon_image)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.klissans = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_klissans()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и событий мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позицию снарядов и уничтожение страрых снарядов"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_klissans(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.klissans.update(self)

    def _create_fleet(self):
        """Создание флота вторжения"""
        klissan = Klissan(self)
        klissan_width, klissan_height = klissan.rect.size
        available_space_x = self.settings.screen_width - (2 * klissan_width)
        number_klissans_x = available_space_x // (2 * klissan_width)

        """Определяет количество рядов, помещающихся на экран"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * klissan_height) - ship_height)
        number_rows = available_space_y // (2 * klissan_height)

        for row_number in range(number_rows):
            for klissan_number in range(number_klissans_x):
                self._create_klissan(klissan_number, row_number)

    def _create_klissan(self, klissan_number, row_number):
        """Создание одного пришельца в ряду"""
        klissan = Klissan(self)
        klissan_width, klissan_height = klissan.rect.size
        klissan.x = klissan_width + 2 * klissan_width * klissan_number
        klissan.rect.x = klissan.x
        klissan.rect.y = klissan.rect.height + 2 * klissan.rect.height * row_number
        self.klissans.add(klissan)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for klissan in self.klissans.sprites():
            if klissan.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for klissan in self.klissans.sprites():
            klissan.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.klissans.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    ai = KlissanInvasion()
    ai.run_game()
