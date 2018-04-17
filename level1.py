import public
import pygame

from commonMinion import CommonMinion
from player import Player
from sprite import Sprite
from tileMap import TileMap


class Level1:

    def __init__(self, manager):
        self.background = Sprite("Resources/Backgrounds/level1.png").get_image(0, 0, public.display_dimensions[0], public.display_dimensions[1])

        self.manager = manager;

        self.player = Player()
        self.player.set_position(250, 254)

        minion1 = CommonMinion()
        minion1.set_movement(300, 278, 300, 500)

        self.enemies = [
            minion1
        ]

        self.tile_map = TileMap("Resources/Maps/level1.map")

    def update(self):
        if self.player.rect.bottom >= public.display_dimensions[1]:
            self.manager.state_index = 0

        self.tile_map.set_exceed(self.player.bound_exceed)
        self.tile_map.update()

        self.player.set_blocks(self.tile_map.blocks)
        self.player.update()

        for enemy in self.enemies:
            enemy.set_exceed(self.player.bound_exceed)
            enemy.update()

        self.player.rect.y += 1
        test_collisions = pygame.sprite.spritecollide(self.player, self.tile_map.blocks, False)

        if test_collisions:
            self.player.rect.bottom = test_collisions[0].rect.top
            self.player.d_y = 0
        else:
            self.player.d_y += self.player.gravity
            self.player.rect.y -= 1

        collisions = pygame.sprite.spritecollide(self.player, self.tile_map.blocks, False)
        for block in collisions:
            if self.player.moving_right:
                self.player.rect.right = block.rect.left
            elif self.player.moving_left:
                self.player.rect.left = block.rect.right

    def draw(self, display):
        display.blit(self.background, (0, 0))
        self.tile_map.draw(display)

        for enemy in self.enemies:
            enemy.draw(display)

        self.player.draw(display)

    def key_pressed(self, key):
        self.player.key_pressed(key)

    def key_released(self, key):
        self.player.key_released(key)
