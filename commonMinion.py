import pygame

from sprite import Sprite


class CommonMinion:

    def __init__(self):
        movement_sprite_sheet = Sprite("Resources/Sprites/snake.png")

        self.right_walk_images = [
            movement_sprite_sheet.get_image(0, 0, 48, 42),
            movement_sprite_sheet.get_image(48, 0, 54, 42)
        ]

        self.left_walk_images = [pygame.transform.flip(image, True, False) for image in self.right_walk_images]

        self.image = self.right_walk_images[0]
        self.image_index = 0
        self.image_rate = 0.05
        self.rect = self.image.get_rect()

        self.move_speed = 2
        self.direction = 0
        self.lower_limit = None
        self.upper_limit = None

        self.bound_exceed = None

    def update(self):
        self.image_index += self.image_rate
        if self.image_index > len(self.right_walk_images):
            self.image_index = 0

        if self.direction == 0:
            self.image = self.right_walk_images[int(self.image_index)]

            if int(self.image_index) == 1:
                self.rect.x += self.move_speed + self.move_speed / 10
            else:
                self.rect.x += self.move_speed

            if self.rect.x > self.upper_limit:
                self.direction = 1
        else:
            self.image = self.left_walk_images[int(self.image_index)]

            if int(self.image_index) == 1:
                self.rect.x -= self.move_speed + self.move_speed / 10
            else:
                self.rect.x -= self.move_speed

            if self.rect.x < self.lower_limit:
                self.direction = 0

    def draw(self, display):
        display.blit(self.image, (self.rect.x + self.bound_exceed, self.rect.y))

    def set_exceed(self, bound_exceed):
        self.bound_exceed = bound_exceed

    def set_movement(self, x, y, lower_limit, upper_limit):
        self.rect.x = x
        self.rect.y = y
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
