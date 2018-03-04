class Block():

	def __init__(self, image, x, y):
		self.image = image

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def getImage(self):
		return self.image

	def getPosition(self):
		return (self.rect.x, self.rect.y)
