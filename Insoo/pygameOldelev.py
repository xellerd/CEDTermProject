import pygame
import sys
from pygame.locals import*
from time import sleep
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 430
WHITE=(255,255,255)
RED=(255,0,0)
BLUE =(0,0,255)
BLACK=(0,0,0)
CAPTION="Oldelevator"
#층수 12층
elevator_width = 30
elevator_height = 10


def drawObject(obj,x,y):
	global gamePad
	gamePad.blit(obj,(x,y))

def dispMessage(text,y):
	global gamePad
	largeText = pygame.font.Font('Rock.ttf',8)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (160,y)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()

def textObject(text,font):
	textSurface = font.render(text,True,BLACK)
	return textSurface, textSurface.get_rect()

def elev1_info(text,passenger):
	global gamePad
	largeText = pygame.font.Font('ROCK.ttf',8)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (150,40)
		# 현재 시간과 passanger[1]이 같아지면 탑승객 정보를 띄운다.
	# passenger = [0id, 1time, 2departure, 3arrival, 4weight,] 5arrivalTime]
	if onlist[1] == time:
		textObject(text,largeText)
		TextRect.center = (160,50)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()

def elev2_info(text):
	global gamePad
	largeText = pygame.font.Font('ROCK.ttf',8)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (150,180)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()

def elev3_info(text):
	global gamePad
	largeText = pygame.font.Font('ROCK.ttf',8)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (150,330)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()
def invertfloor(floor):
	y = [o1_y,o2_y,o3_y,n1_y,n2_y,n3_y]
	if floor == 1 :
		y = 400
	elif floor == 2 :
		y = 370
	elif floor == 3 :
	elif floor == 4 :
	elif floor == 5 :
	elif floor == 6 :
	elif floor == 7 :
	elif floor == 8 :
	elif floor == 9 :
	elif floor == 10 :
	elif floor == 11 :

def move(): # rungame()
	global clock, gamePad, elevator1,elevator2,elevator3
	passanger_count=0
	elevator_xy=[]
	gamePad.fill(WHITE)
	o1_y=400
	o2_y=400
	o3_y=400

	n1_y= 400
	n2_y= 400
	n3_y= 400



	#엘리베이터 루프
	while True:
		#elev 시스템 종료
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		#elev 알고리즘 방향키 위 누르면 t실행해보는걸로 하자
		# if pressed[pygame.K_UP]:
			#다다다다다다다닥
		#Ver1 보면 아마 에리베이터 위치도 초기화 되어 있을 것이당.
		# b1_y = ev1.Invertfloor(floor)
		# b2_y = ev2.Invertfloor(floor)
		# b3_y = ev3.Invertfloor(floor)

		o1 = {'rect':pygame.Rect(10,o1_y,elevator_height,elevator_width)}
		o2 = {'rect':pygame.Rect(40,o2_y,elevator_height,elevator_width)}
		o3 = {'rect':pygame.Rect(70,o3_y,elevator_height,elevator_width)}
		Oldboxes =[o1,o2,o3]
		for b1 in Oldboxes:
			pygame.draw.rect(gamePad,RED, b1['rect'])
		n1 = {'rect':pygame.Rect(380,n1_y,elevator_height,elevator_width)}
		n2 = {'rect':pygame.Rect(410,n2_y,elevator_height,elevator_width)}
		n3 = {'rect':pygame.Rect(440,n3_y,elevator_height,elevator_width)}
		Newboxes =[n1,n2,n3]
		for b2 in Newboxes:
			pygame.draw.rect(gamePad,RED,b2['rect'])


		floor_end=[400,370,340,310,280,250,220,190,160,130,100,70]
		for h in floor_end:	
			pygame.draw.line(gamePad, BLACK, (0,h),(100,h),1)
			pygame.draw.line(gamePad, BLACK, (360,h),(450,h),1)
		pygame.draw.line(gamePad, BLACK, (100,10),(100,490),3)
		pygame.draw.line(gamePad, BLACK, (360,10),(360,490),3)




		dispMessage('ELEVATOR_01', 20)
		dispMessage('ELEVATOR_02',150)
		dispMessage('ELEVATOR_03',290)
			#엘리베이터 업무표.destlist[] + 타있는 passenger 정보.
		# elev1_info(ev1.listToAdd)
		# elev2_info(ev2.listToAdd)
		# elev3_info(ev3.listToAdd)

		pygame.draw.line(gamePad, BLACK, (150,390),(300,390),1)
		dispMessage('Throughput = ', 400)
			#기욱씨 임시 인스턴스의 경우 소욧시간변수(=tempEV1,tempEV2,tempEV3)
			#영준형 임시 인스턴스의 경우 소욧시간변수(=)
		# Throughput = passenger_count * arrivaltime_all / 설정time 
		# dispMessage(Throughput, 410)

		pygame.display.update()
		clock.tick(60)
	pygame.quit()
	quit()

def initGame():
	global clock, gamePad,elevator
	pygame.init()
	gamePad = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption(CAPTION)

	
	clock = pygame.time.Clock()
	move()


if __name__=='__main__':
	initGame()