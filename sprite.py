import public
import pygame

class Sprite():

	def __init__(self, filePath):
		self.spriteSheet = pygame.image.load(filePath)

	def getImage(self, x, y, width, height):
		image = pygame.Surface((width, height)).convert()
		image.blit(self.spriteSheet, (0, 0), (x, y, width, height))
		image.set_colorkey((0, 0, 0))

		return image

	def getSize(self):
		return self.spriteSheet.get_rect()
