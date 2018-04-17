import public
import pygame

from sprite import Sprite


class GameOver:

    def __init__(self):
        self.background = Sprite("Resources/Backgrounds/end.png").get_image(0, 0, public.display_dimensions[0], public.display_dimensions[1])
        self.message = pygame.font.Font("Resources/Fonts/arial.ttf", 30).render("Press ENTER to exit...", True, (243, 104, 59))

    def update(self):
        pass

    def draw(self, display):
        display.fill((0, 0, 0))
        display.blit(self.background, (0, 0))
        display.blit(self.message, (150, 225))

    def key_pressed(self, key):
        if key == 13:
            quit()

    def key_released(self, key):
        pass
