import constant
import pygame

from manager import Manager

def main():

	pygame.init()
	pygame.display.set_caption(constant.title)

	clock = pygame.time.Clock()
	display = pygame.display.set_mode(constant.displayDimensions)
	manager = Manager()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				manager.keyPressed(pygame.key.name(event.key))
			elif event.type == pygame.KEYUP:
				manager.keyReleased(pygame.key.name(event.key))

		manager.update()
		manager.draw(display)

		pygame.display.flip()
		clock.tick(constant.fps)

if __name__ == "__main__":
	main()
