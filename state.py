import public
import pygame

from player import Player
from sprite import Sprite
from tileMap import TileMap

class Menu():

	def __init__(self):
		background = Sprite("Resources/Backgrounds/menu.png")
		self.background = background.getImage(0, 0, public.displayDimensions[0], public.displayDimensions[1])
		self.backgroundX = 0

		self.title = pygame.font.Font("Resources/Fonts/centurygothic.ttf", 70).render(public.title, True, (128, 0, 0))

		self.currentOption = 0
		self.optionAttributes = [
			("Start", (270, 240)),
			("Help", (275, 280)),
			("Quit", (275, 320))
		]

	def update(self):
		self.backgroundX += 0.5
		if self.backgroundX == public.displayDimensions[0]:
			self.backgroundX = 0

	def draw(self, display):
		display.blit(self.background, (self.backgroundX, 0))
		display.blit(self.background, (self.backgroundX - public.displayDimensions[0], 0))

		display.blit(self.title, (120, 70))

		for option in self.optionAttributes:
			color = (255, 0, 0) if self.currentOption == self.optionAttributes.index(option) else (0, 0, 0)
			display.blit(pygame.font.Font("Resources/Fonts/arial.ttf", 30).render(option[0], True, color), option[1])

	def keyPressed(self, key):
		if key == "w":
			self.currentOption -= 1
			if self.currentOption < 0:
				self.currentOption = len(self.optionAttributes) - 1
		elif key == "s":
			self.currentOption += 1
			if self.currentOption == len(self.optionAttributes):
				self.currentOption = 0
		elif key == "return":
			if self.currentOption == 0:
				public.currentState = 1
			elif self.currentOption == 2:
				quit()

	def keyReleased(self, key):
		pass

class Level1():

	def __init__(self):
		background = Sprite("Resources/Backgrounds/level1.png")
		self.background = background.getImage(0, 0, public.displayDimensions[0], public.displayDimensions[1])

		self.tileMap = TileMap("Resources/Maps/level1.map")

		self.player = Player()
		self.player.setStartPosition(297, 255)

	def update(self):
		self.player.update()
		self.tileMap.update()

	def draw(self, display):
		display.blit(self.background, (0, 0))
		self.tileMap.draw(display)
		self.player.draw(display)

	def keyPressed(self, key):
		self.player.keyPressed(key)

	def keyReleased(self, key):
		self.player.keyReleased(key)
