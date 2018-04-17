import public
import pygame

from manager import Manager

pygame.font.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode(public.display_dimensions)
manager = Manager()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            manager.key_pressed(event.key)
        elif event.type == pygame.KEYUP:
            manager.key_released(event.key)
        elif event.type == pygame.QUIT:
            quit()

    manager.update()
    manager.draw(display)

    pygame.display.flip()
    clock.tick(public.fps)
