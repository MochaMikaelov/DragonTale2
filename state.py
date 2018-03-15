import constant
import pygame

from player import Player
from sprite import Sprite
from tileMap import TileMap

class Level1State():

	def __init__(self):
		self.background = Sprite("Resources/Backgrounds/level1.png")

		self.player = Player()
		self.player.setStartPosition(297, 255)

		self.tileMap = TileMap(64, "Resources/Sprites/tiles.png", "Resources/Maps/level1.map")

		constant.fps = 60

	def update(self):
		self.player.update()
		self.tileMap.setOffset(self.player.getBoundExceed())

	def draw(self, display):
		self.background.draw(display)
		self.tileMap.draw(display)
		self.player.draw(display)

	def keyPressed(self, key):
		self.player.keyPressed(key)

	def keyReleased(self, key):
		self.player.keyReleased(key)

class MenuState():

	def __init__(self, manager):
		self.background = Sprite("Resources/Backgrounds/menu.png")
		self.background.setVector(0.5, 0)

		self.currentOption = 0

		self.manager = manager

		self.optionAttributes = [
			("Start", (270, 240)),
			("Help", (275, 280)),
			("Quit", (275, 320))
		]

		self.title = pygame.font.Font("Resources/Fonts/centurygothic.ttf", 70).render(constant.title, True, (128, 0, 0))

		constant.fps = 15

	def update(self):
		self.background.update()

	def draw(self, display):
		self.background.draw(display)

		display.blit(self.title, (80, 70))

		for i in range(len(self.optionAttributes)):
			color = (255, 0, 0) if self.currentOption == i else (0, 0, 0)
			display.blit(pygame.font.Font("Resources/Fonts/arial.ttf", 30).render(self.optionAttributes[i][0], True, color), (self.optionAttributes[i][1]))

	def keyPressed(self, key):
		if key == "w":
			self.currentOption -= 1
		elif key == "s":
			self.currentOption += 1
		elif key == "return":
			if self.currentOption == 0:
				self.manager.setState(1)
			elif self.currentOption == 2:
				pygame.quit()
				quit()

		self.currentOption = len(self.optionAttributes) - 1 if self.currentOption < 0 else self.currentOption
		self.currentOption = 0 if self.currentOption == len(self.optionAttributes) else self.currentOption

	def keyReleased(self, key):
		pass
