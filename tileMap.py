import constant
import re

from block import Block
from sprite import Sprite

class TileMap():

	def __init__(self, tileSize, tilePath, mapPath):
		tileSize = tileSize




		#LOAD TILE IMAGES
		tileSheet = Sprite(tilePath)

		self.tileImages = []
		for i in range(int(tileSheet.getSize().width / tileSize)):
			self.tileImages.append(tileSheet.getImage(tileSize * i, 0, tileSize, tileSize))




		#LOAD TILE MAP
		lines = [line.rstrip("\n") for line in open(mapPath)]
		self.numberOfColumns = int(lines[0])
		self.numberOfRows = int(lines[1])

		self.imageMap = []
		for i in range(self.numberOfRows):
			self.imageMap.append(re.findall("\d+", lines[i + 2]))



		#LOAD COLLISION MAP
		self.collisionMap = []
		for i in range(self.numberOfRows):
			self.collisionMap.append(re.findall("\d+", lines[i + 2 + self.numberOfRows]))



		#CREATE BLOCKS
		self.blockMap = []
		for a in range(self.numberOfRows):
			for b in range(self.numberOfColumns):
				if int(self.collisionMap[a][b]) == 1:
					block = Block(self.tileImages[int(self.imageMap[a][b]) - 1], b * tileSize, a * tileSize)
					self.blockMap.append(block)

	def update(self):
		pass

	def draw(self, display):
		for block in self.blockMap:
			display.blit(block.getImage(), block.getPosition())
