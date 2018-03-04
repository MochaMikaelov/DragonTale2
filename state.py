import constant
import pygame

from abc import ABC, abstractmethod
from player import Player
from sprite import Sprite
from tileMap import TileMap

class State(ABC):

	@abstractmethod
	def __init__(self, manager):
		pass

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def draw(self, display):
		pass

	@abstractmethod
	def keyPressed(self, key):
		pass

	@abstractmethod
	def keyReleased(self, key):
		pass

class Level1State(State):

	def __init__(self, manager):
		self.manager = manager

		self.background = Sprite("Resources/Backgrounds/level1.png")
		self.background.setPosition(0, 0)

		self.tileMap = TileMap(64, "Resources/Sprites/tiles.png", "Resources/Maps/level1.map")

	def update(self):
		pass

	def draw(self, display):
		self.background.draw(display)
		self.tileMap.draw(display)

	def keyPressed(self, key):
		pass

	def keyReleased(self, key):
		pass

class MenuState(State):

	def __init__(self, manager):
		self.manager = manager

		self.background = Sprite("Resources/Backgrounds/menu.png")
		self.background.setPosition(0, 0)
		self.background.setVector(0.5, 0)

		self.title = pygame.font.Font(constant.menuTitleFont, constant.menuTitleFontSize).render(constant.title, True, constant.menuTitleColor)

		self.optionAttributes = [
			("Start", (270, 240)),
			("Help", (275, 280)),
			("Quit", (275, 320))
		]

		self.optionColors = [
			constant.menuOptionColorNormal,
			constant.menuOptionColorNormal,
			constant.menuOptionColorNormal
		]

		self.currentOption = 0

	def update(self):
		self.background.update()
		self.optionRecolor()

	def draw(self, display):
		self.background.draw(display)

		display.blit(self.title, (80, 70))

		for i in range(len(self.optionAttributes)):
			option = pygame.font.Font(constant.menuOptionFont, constant.menuOptionFontSize).render(self.optionAttributes[i][0], True, self.optionColors[i])
			display.blit(option, self.optionAttributes[i][1])

	def keyPressed(self, key):
		if key == "w":
			self.currentOption -= 1
		elif key == "s":
			self.currentOption += 1
		elif key == "return":
			if self.currentOption == 0:
				self.manager.setState(2)
			elif self.currentOption == 1:
				self.manager.setState(1)
			elif self.currentOption == 2:
				pygame.quit()
				quit()

		if self.currentOption < 0:
			self.currentOption = len(self.optionAttributes) - 1
		elif self.currentOption == len(self.optionAttributes):
			self.currentOption = 0

	def keyReleased(self, key):
		pass

	def optionRecolor(self):
		for i in range(len(self.optionAttributes)):
			self.optionColors[i] = constant.menuOptionColorNormal

		self.optionColors[self.currentOption] = constant.menuOptionColorSelected

class OptionState(State):

	def __init__(self, manager):
		self.manager = manager

		self.background = Sprite("Resources/Backgrounds/option.png")
		self.background.setPosition(0, 0)

	def update(self):
		pass

	def draw(self, display):
		self.background.draw(display)

	def keyPressed(self, key):
		pass

	def keyReleased(self, key):
		pass
