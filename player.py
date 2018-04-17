import public
import pygame

from sprite import Sprite


class Player:

    def __init__(self):
        movement_sprite_sheet = Sprite("Resources/Sprites/player.png")

        self.right_walk_images = [
            movement_sprite_sheet.get_image(0, 0, 45, 66),
            movement_sprite_sheet.get_image(45, 0, 45, 66),
            movement_sprite_sheet.get_image(93, 0, 45, 66),
            movement_sprite_sheet.get_image(138, 0, 50, 66)
        ]

        self.left_walk_images = [pygame.transform.flip(image, True, False) for image in self.right_walk_images]

        self.image = self.right_walk_images[0]
        self.image_index = 0
        self.image_rate = 0.1
        self.rect = self.image.get_rect()

        self.moving_left = False
        self.moving_right = False
        self.move_speed = 5

        self.d_y = 0
        self.gravity = 0.45
        self.jump_height = 8

        self.right_limit = public.display_dimensions[0] * 0.6
        self.left_limit = public.display_dimensions[0] * 0.4 - self.rect.width

        self.bound_exceed = 0

        self.blocks = None

    def update(self):
        self.rect.y += self.d_y

        if self.moving_right or self.moving_left:
            self.image_index += self.image_rate
            if self.image_index > len(self.right_walk_images) - 1:
                self.image_index = 0

            if self.moving_right:
                self.image = self.right_walk_images[int(self.image_index)]
            else:
                self.image = self.left_walk_images[int(self.image_index)]

            if self.moving_right:
                if self.rect.x >= self.right_limit:
                    self.rect.x = self.right_limit
                    self.bound_exceed -= self.move_speed
                else:
                    self.rect.x += self.move_speed
            else:
                if self.rect.x <= self.left_limit:
                    self.rect.x = self.left_limit
                    self.bound_exceed += self.move_speed
                else:
                    self.rect.x -= self.move_speed

        current_pos = (self.rect.x, self.rect.y)
        self.rect = self.image.get_rect()
        self.rect.x = current_pos[0]
        self.rect.y = current_pos[1]

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def key_pressed(self, key):
        if key == 100:
            self.moving_right = True
        elif key == 97:
            self.moving_left = True
        elif key == 119 and self.d_y == 0:
            self.d_y = -self.jump_height

    def key_released(self, key):
        if key == 100:
            self.moving_right = False
        elif key == 97:
            self.moving_left = False

    def set_blocks(self, blocks):
        self.blocks = blocks

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

