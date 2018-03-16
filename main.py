import public
import pygame

from state import  Level1, Menu

def main():

	pygame.init()
	pygame.display.set_caption(public.title)

	clock = pygame.time.Clock()
	display = pygame.display.set_mode(public.displayDimensions)

	states = [
		Menu(),
		Level1()
	]

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				states[public.currentState].keyPressed(pygame.key.name(event.key))
			elif event.type == pygame.KEYUP:
				states[public.currentState].keyReleased(pygame.key.name(event.key))
			elif event.type == pygame.QUIT:
				quit()

		states[public.currentState].update()
		states[public.currentState].draw(display)

		pygame.display.flip()
		clock.tick(public.fps)

if __name__ == "__main__":
	main()

#TODO simplify event loop in main()
#TODO simplify Menu.keyPressed()
#TODO make a text centering mechanism for options and title in Menu.draw()
#TODO optimise/simplify Level1().init(), Level1().update(), Level1().draw()
