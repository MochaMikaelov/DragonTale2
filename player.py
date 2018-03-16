import public

from sprite import Sprite

class Player():

	def __init__(self):
		movementSpriteSheet = Sprite("Resources/Sprites/player.png")

		self.rightWalkImages = [
			movementSpriteSheet.getImage(0, 0, 45, 66),
			movementSpriteSheet.getImage(45, 0, 45, 66),
			movementSpriteSheet.getImage(93, 0, 45, 66),
			movementSpriteSheet.getImage(138, 0, 50, 66)
		]

		self.image = self.rightWalkImages[0]
		self.rect = self.image.get_rect()

		self.moveLeft = False
		self.moveRight = False

	def setStartPosition(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def update(self):
		if self.moveRight:
			if self.rect.x >= public.displayDimensions[0] * 0.6:
				self.rect.x = public.displayDimensions[0] * 0.6
				public.boundExceed -= 5
			else:
				self.rect.x += 5
		elif self.moveLeft:
			if self.rect.x <= public.displayDimensions[0] * 0.4 - self.rect.width:
				self.rect.x = public.displayDimensions[0] * 0.4 - self.rect.width
				public.boundExceed += 5
			else:
				self.rect.x -= 5

	def draw(self, display):
		display.blit(self.image, (self.rect.x, self.rect.y))

	def keyPressed(self, key):
		if key == "d":
			self.moveRight = True
		elif key == "a":
			self.moveLeft = True

	def keyReleased(self, key):
		if key == "d":
			self.moveRight = False
		elif key == "a":
			self.moveLeft = False
