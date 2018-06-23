import sys, pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode(200, 200)

pygame.display.set_caption('elev visualize')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

o1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED}

boxes = [o1]

DISPLAYSURF.fill(WHITE)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		for b in boxes:
			b['rect'].top = floor

			pygame.draw.rect(DISPLAYSURF, b['color'], b['rect'])

	pygame.display.update()
	time.sleep(1)
