import constant
import pygame

class Sprite(object):

	def __init__(self, filePath):
		self.spriteSheet = pygame.image.load(filePath)
		self.x = 0
		self.y = 0

	def getImage(self, x, y, width, height):
		image = pygame.Surface((width, height)).convert()
		image.blit(self.spriteSheet, (0, 0), (x, y, width, height))
		image.set_colorkey((0, 0, 0))

		return image

	def getSize(self):
		return self.spriteSheet.get_rect()

	def setVector(self, xChange, yChange):
		self.xChange = xChange
		self.yChange = yChange

	def update(self):
		self.x += self.xChange
		self.y += self.yChange

	def draw(self, display):
		display.blit(self.spriteSheet, (self.x, self.y))

		if self.x < 0:
			display.blit(self.spriteSheet, (self.x + constant.displayDimensions[0], self.y))
		elif self.x > 0:
			display.blit(self.spriteSheet, (self.x - constant.displayDimensions[0], self.y))
