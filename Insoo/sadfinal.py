import pygame
import sys
from time import sleep
from pygame.locals import*
import oodEv_final

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 430
WHITE=(255,255,255)
RED=(255,0,0)
BLUE =(0,0,255)
BLACK=(0,0,0)
CAPTION="Oldelevator"

elevator_width = 30
elevator_height = 10

TARGET_FPS = 1
clock = pygame.time.Clock()

def drawObject(obj,x,y):
	global gamePad
	gamePad.blit(obj,(x,y))


def textObject(text,font):
	textSurface = font.render(text,True,BLACK)
	return textSurface, textSurface.get_rect()

def dispMessage(text,y):
	global gamePad
	largeText = pygame.font.Font('Rock.ttf',10)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (225,y)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()

def drawClock(count):
	global gamePad, clockcount
	
	font = pygame.font.Font('Rock.ttf', 10)
	text = font.render('Clock:'+str(count),True,BLACK)
	gamePad.blit(text,(0,0))

def invertfloor(floor):
	floor = 400-30*(floor-1)
	return floor


def rungame():
	global clock, gamePad,passengerList

	clock_count=0
	gamePad.fill(WHITE)
	
	ins_n1 = oodEv_final.Elevator()
	ins_n2 = oodEv_final.Elevator()
	ins_n3 = oodEv_final.Elevator()
	

	dispMessage('o1 ,n1',20)
	dispMessage('o2 ,n2',150)
	dispMessage('o3 ,n3',280)

	floor_end=[400,370,340,310,280,250,220,190,160,130,100,70]
	for h in floor_end:	
		pygame.draw.line(gamePad, BLACK, (0,h),(100,h),1)
		pygame.draw.line(gamePad, BLACK, (360,h),(450,h),1)
	pygame.draw.line(gamePad, BLACK, (100,10),(100,490),3)
	pygame.draw.line(gamePad, BLACK, (360,10),(360,490),3)
	pygame.draw.line(gamePad, BLACK, (150,390),(300,390),1)
	dispMessage('Throughput = ', 400)

	# <<<throughput  계산식>>>>
	# totaltime = passengerList[0].[3]- passengerList[0].[2]
	# passengercount += passengerList[1]
	# throughput = totaltime * passengercount
	t=0
	while True:
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		passengerList = [oodEv_final.Passenger(1, 2, 3, 6), oodEv_final.Passenger(2,5,7,2)]	
		passengerIndex = oodEv_final.passengerSearch(passengerList, t)
		passenger = passengerList[passengerIndex]

		if passengerIndex != -1:
			oodEv_final.evCall(ins_n1,ins_n2,ins_n3,passenger)


		ins_n1.move(int(round(pygame.time.get_ticks()/1000)))
		ins_n2.move(int(round(pygame.time.get_ticks()/1000)))
		ins_n3.move(int(round(pygame.time.get_ticks()/1000)))

		n1 =  {'rect':pygame.Rect(370,invertfloor(ins_n1.floor),elevator_height, elevator_width)}
		n2 =  {'rect':pygame.Rect(400,invertfloor(ins_n2.floor),elevator_height, elevator_width)}
		n3 =  {'rect':pygame.Rect(430,invertfloor(ins_n3.floor),elevator_height, elevator_width)}
		Newboxes =[n1,n2,n3]
		for b2 in Newboxes:
			pygame.draw.rect(gamePad,RED,b2['rect'])


		data = "%d\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n" % (t, ins_n1.floor, ins_n1.dir, ins_n1.passenger, ins_n2.floor, ins_n2.dir, ins_n2.passenger, ins_n3.floor, ins_n3.dir, ins_n3.passenger)
		dispMessage(data, 60)
		t = t+1
		print(t)
		# dispMessage(throughput, 400)
		pygame.display.update()
		clock.tick(TARGET_FPS)
		
	pygame.quit()
	quit()
def initGame():
	global clock, gamePad, Elevator



	pygame.init()
	gamePad = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	pygame.display.set_caption(CAPTION)
	rungame()

if __name__=='__main__':
	initGame()