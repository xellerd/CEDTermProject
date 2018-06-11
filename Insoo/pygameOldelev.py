import pygame
from pygame.locals import*
from time import sleep
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 1200
WHITE=(255,255,255)
RED=(255,0,0)
BLUE =(0,0,255)
CAPTION="Oldelevator"
#층수 12층
elevator_width = 50
elevator_height = 100
UPRIGHT = 'upright'

waittime = 5
uptime=5
downtime=5
elevlocation = 1100



def drawObject(obj,x,y):
	global gamePad
	gamePad.blit(obj,(x,y))

def textObject(text,font):
	textSurface = font.render(text,True,RED)
	return textSurface, textSurface.get_rect()

def dispMessage(text):
	global gamePad
	largeText = pygame.font.Font('GILLUBCD.ttf',10)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (400,10)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()
	sleep(1)
	move()

def input_in():
	dispMessage('%d층에서 %d명이 %d방향 호출',floor,passanger,direction) #변수명에 따라 조정필요
def input_out():
	# move에 추가해줘야할 내용 : if 
def move(): # rungame()
	global clock, gamePad, elevator1,elevator2,elevator3
	passanger_count=0
	elevator_xy=[]
	gamePad.fill(WHITE)
	b1_y=10
	b2_y=10
	b3_y=10

	#엘리베이터 루프
	while True:
		#elev 시스템 종료
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finish=True
		#elev 알고리즘 방향키 위 누르면
		# if pressed[pygame.K_UP]:
			#다다다다다다다닥



		b1 = {'rect':pygame.Rect(0,b1_y,elevator_height,elevator_width)}
		b2 = {'rect':pygame.Rect(150,b2_y,elevator_height,elevator_width)}
		b3 = {'rect':pygame.Rect(300,b3_y,elevator_height,elevator_width)}
		boxes =[b1,b2,b3]
		for b in boxes:
			pygame.draw.rect(gamePad,RED, b['rect'])

		# if Movelist[] != None:
		# 	if direction == 1 : 
		# 		sleep(2)
		# 		elevlocation ++
						

		# 		Movelist[]= upfloor[]+destination[]
		# 		Movelist[].sort()
		# 		if  elevlocation>floor:
		# 			upfloor[].append(floor)

		# 		elif elevlocation in Movelist[]:
		# 			elevlocation = elevlocation
		# 			elevator.printinfo()
		# 			sleep(5)
		# 		else:
		# 			pass
						



		# 	elif direction == -1:
		# 		sleep(2)
		# 		elevlocation --
		# 		Movelist[]= downfloor[]+destination[]
		# 		Movelist[].sort()
		# 		if elevlocation<floor:
		# 			downfloor[].append(floor)
		# 			elif elevlocation in Movelist[]:
		# 			elevlocation = elevlocation
		# 			elevator.printinfo()
		# 			sleep(5)
		# 		else:
		# 			pass
		# elif Movelist[] ==None:
		# 	elevlocation = elevlocation
		
		pygame.display.update()
		clock.tick(60)
	pygame.quit()
	quit()

def initGame():
	global clock, gamePad,elevator
	pygame.init()
	gamePad = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	# elevator1 = pygame.draw.rect(gamePad, RED,(20,200,elevator_width,elevator_height))
	# elevator2 = pygame.draw.rect(gamePad, RED,(50,200,elevator_width,elevator_height))
	# elevator3 = pygame.draw.rect(gamePad, RED,(80,200,elevator_width,elevator_height))

	pygame.display.set_caption(CAPTION)
	floor_1 = elevlocation
	
	clock = pygame.time.Clock()
	move()


if __name__=='__main__':
	initGame()