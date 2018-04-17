import public
import pygame

from sprite import Sprite


class Menu:

    def __init__(self, manager):
        self.background = Sprite("Resources/Backgrounds/menu.png").get_image(0, 0, public.display_dimensions[0], public.display_dimensions[1])
        self.background_x = 0

        self.manager = manager

        self.options = [
            "Start",
            "Help",
            "Quit"
        ]
        self.option_colors = [
            (255, 0, 0),
            (0, 0, 0),
            (0, 0, 0)
        ]
        self.option_index = 0

        self.title = pygame.font.Font("Resources/Fonts/centurygothic.ttf", 70).render(public.title, True, (128, 0, 0))
        self.titleRect = self.title.get_rect(centerx=public.display_dimensions[0] / 2)

    def update(self):
        self.background_x += 1
        if self.background_x == public.display_dimensions[0]:
            self.background_x = 0

    def draw(self, display):
        display.blit(self.background, (self.background_x, 0))
        display.blit(self.background, (self.background_x - public.display_dimensions[0], 0))

        display.blit(self.title, (self.titleRect.x, 70))

        for option in self.options:
            button = pygame.font.Font("Resources/Fonts/arial.ttf", 30).render(option, True, self.option_colors[self.options.index(option)])
            button_rect = button.get_rect(centerx=public.display_dimensions[0] / 2)
            display.blit(button, (button_rect.x, 40 * self.options.index(option) + 240))

    def key_pressed(self, key):
        if key == 115:
            self.option_index += 1
            if self.option_index == len(self.options):
                self.option_index = 0
        elif key == 119:
            self.option_index -= 1
            if self.option_index < 0:
                self.option_index = len(self.options) - 1
        elif key == 13:
            if self.option_index == 0:
                self.manager.state_index = 2
            elif self.option_index == 2:
                quit()

        for option in self.options:
            if self.option_index == self.options.index(option):
                self.option_colors[self.options.index(option)] = (255, 0, 0)
            else:
                self.option_colors[self.options.index(option)] = (0, 0, 0)

    def key_released(self, key):
        pass
