import public

from block import Block
from sprite import Sprite


class TileMap:

    def __init__(self, map_path):
        tile_sheet = Sprite("Resources/Sprites/tiles.png")
        self.tile_images = [tile_sheet.get_image(public.tile_size * i, 0, public.tile_size, public.tile_size) for i in range(tile_sheet.sprite_sheet.get_rect().width // public.tile_size)]

        self.lines = [[int(num) for num in line.strip("\n").split(" ")] for line in open(map_path)]

        self.touchable_map = [self.lines[i + 3] for i in range(self.lines[2][0])]
        self.untouchable_maps = [[self.lines[3 + self.lines[2][0] + (a * self.lines[2][0]) + b] for b in range(self.lines[2][0])] for a in range(self.lines[0][0])]

        self.blocks = []

        self.bound_exceed = None

    def update(self):
        self.blocks.clear()

        for a in range(self.lines[1][0]):
            if a < -self.bound_exceed / public.tile_size - 1 or a > public.display_dimensions[0] / public.tile_size - self.bound_exceed / public.tile_size:
                continue
            for b in range(self.lines[2][0]):
                if self.touchable_map[b][a] != 0:
                    self.blocks.append(Block(self.tile_images[int(self.touchable_map[b][a]) - 1], a * public.tile_size + self.bound_exceed, b * public.tile_size))

    def draw(self, display):
        for a in range(self.lines[0][0]):
            for b in range(self.lines[1][0]):
                if b < -self.bound_exceed / public.tile_size - 1 or b > public.display_dimensions[0] / public.tile_size - self.bound_exceed / public.tile_size:
                    continue
                for c in range(self.lines[2][0]):
                    if self.untouchable_maps[a][c][b] != 0:
                        display.blit(self.tile_images[self.untouchable_maps[a][c][b] - 1], (b * public.tile_size + self.bound_exceed, c * public.tile_size))

        for a in range(self.lines[1][0]):
            if a < -self.bound_exceed / public.tile_size - 1 or a > public.display_dimensions[0] / public.tile_size - self.bound_exceed / public.tile_size:
                continue
            for b in range(self.lines[2][0]):
                if self.touchable_map[b][a] != 0:
                    display.blit(self.tile_images[self.touchable_map[b][a] - 1], (a * public.tile_size + self.bound_exceed, b * public.tile_size))

    def set_exceed(self, bound_exceed):
        self.bound_exceed = bound_exceed
