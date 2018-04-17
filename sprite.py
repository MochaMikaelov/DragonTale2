import pygame


class Sprite:

    def __init__(self, file_path):
        self.sprite_sheet = pygame.image.load(file_path)

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height)).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))

        return image
