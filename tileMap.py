import constant
import re

from sprite import Sprite

class TileMap():

	def __init__(self, tileSize, tilePath, mapPath):
		self.tileSize = tileSize

		tileSheet = Sprite(tilePath)
		self.tileImages = []
		for i in range(int(tileSheet.getSize().width / self.tileSize)):
			self.tileImages.append(tileSheet.getImage(self.tileSize * i, 0, self.tileSize, self.tileSize))

		lines = [line.rstrip("\n") for line in open(mapPath)]
		self.numberOfMaps = int(lines[0])
		self.numberOfColumns = int(lines[1])
		self.numberOfRows = int(lines[2])

		self.touchableMap = []
		for i in range(self.numberOfRows):
			self.touchableMap.append(re.findall("\d+", lines[i + 3]))

		self.untouchableMaps = []
		for a in range(self.numberOfMaps):
			untouchableMap = []
			for b in range(self.numberOfRows):
				untouchableMap.append(re.findall("\d+", lines[3 + self.numberOfRows + (a * self.numberOfRows) + b]))
			self.untouchableMaps.append(untouchableMap)

		self.offset = 0

	def setOffset(self, offset):
		self.offset = offset

	def update(self):
		pass

	def draw(self, display):
		for a in range(self.numberOfMaps):
			for b in range(self.numberOfRows):
				for c in range(self.numberOfColumns):
					if not self.untouchableMaps[a][b][c] == "0":
						display.blit(self.tileImages[int(self.untouchableMaps[a][b][c]) - 1], (c * self.tileSize + self.offset, b * self.tileSize))

		for a in range(self.numberOfColumns):
			for b in range(self.numberOfRows):
				if not self.touchableMap[b][a] == "0":
					display.blit(self.tileImages[int(self.touchableMap[b][a]) - 1], (a * self.tileSize + self.offset, b * self.tileSize))
