import public
import re

from block import Block
from sprite import Sprite

class TileMap():

	def __init__(self, mapPath):
		tileSheet = Sprite("Resources/Sprites/tiles.png")

		self.tileImages = []
		for i in range(tileSheet.getSize().width // public.tileSize):
			self.tileImages.append(tileSheet.getImage(public.tileSize * i, 0, public.tileSize, public.tileSize))

		self.lines = [line.strip("\n") for line in open(mapPath)]

		self.touchableMap = []
		for i in range(int(self.lines[2])):
			self.touchableMap.append([int(s) for s in self.lines[i + 3].split() if s.isdigit()])

		self.untouchableMaps = []
		for a in range(int(self.lines[0])):
			untouchableMap = []
			for b in range(int(self.lines[2])):
				untouchableMap.append([int(s) for s in self.lines[3 + int(self.lines[2]) + (a * int(self.lines[2])) + b].split() if s.isdigit()])
			self.untouchableMaps.append(untouchableMap)

	def update(self):
		pass

	def draw(self, display):
		blockMap = []
		for a in range(int(self.lines[0])):
			for b in range(int(self.lines[1])):
				if b > 9 - int(public.boundExceed / 64):
					continue
				elif b < 1 - int(public.boundExceed / 64):
					continue
				for c in range(int(self.lines[2])):
					if not self.untouchableMaps[a][c][b] == 0:
						display.blit(self.tileImages[int(self.untouchableMaps[a][c][b]) - 1], (b * public.tileSize + public.boundExceed, c * public.tileSize))
					if not self.touchableMap[c][b] == 0:
						blockMap.append(Block(self.tileImages[int(self.touchableMap[c][b]) - 1], b * public.tileSize + public.boundExceed, c * public.tileSize))

		for block in blockMap:
			display.blit(block.getImage(), block.getPosition())
