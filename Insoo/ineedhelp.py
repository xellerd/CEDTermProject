# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import*
from time import sleep
import oodEv_final

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 430
WHITE=(255,255,255)
RED=(255,0,0)
BLUE =(0,0,255)
BLACK=(0,0,0)
CAPTION="Oldelevator"

# 층수 12층
elevator_width = 30
elevator_height = 10
#
TARGET_FPS = 1
clock = pygame.time.Clock()


#


#

#
def drawClock(count):
	global gamePad, clockcount

	font = pygame.font.Font('Rock.ttf', 8)
	text = font.render('Clock:'+str(count),True,BLACK)
	gamePad.blit(text,(0,0))


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


def elev_info(text,passenger,replace):
	global gamePad
	largeText = pygame.font.Font('ROCK.ttf',8)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (150,40)
		# 현재 시간과 passanger[1]이 같아지면 탑승객 정보를 띄운다.
	# passenger = [0id, 1time, 2departure, 3arrival, 4weight,] 5arrivalTime]
	# 0614_ id대신에  탑승시간으로 적용.

	#만약 시간이 onlist 1번인 time과 같아지면 문자열 출력.
	if onlist[1] == clock:
		textObject(text,largeText)
		TextRect.center = (160,replace)
	gamePad.blit(TextSurf, TextRect)
	pygame.display.update()


def invertfloor(floor):
	# floor y좌표로 바꿔주기
	# floor_end=[400,370,340,310,280,250,220,190,160,130,100,70]
	floor = 400-30*(floor-1)
	return floor


def rungame(): # rungame()
	global clock, gamePad, elevator1,elevator2,elevator3,passenger_list
	passanger_count=0
	elevator_xy=[]
	gamePad.fill(WHITE)
	clockcount =0
	#passanger_list(time, weight, departure, arrival)
<<<<<<< HEAD
	passenger_list = [oodEv_final.Passenger(1, 2, 3, 6), oodEv_final.Passenger(12, 3, 7, 8),oodEv_final.Passenger(11,15,1,5),oodEv_final.Passenger(2,10,3,7),oodEv_final.Passenger(5,10,10,5)]
	
=======
	passenger_list = [oodEv_final.Passenger(1, 2, 3, 6), oodEv_final.Passenger(12, 3, 7, 8)]

>>>>>>> e413017a78e66348bc89cea870d35e2d581cc9f5
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
		#  if event.type == KEYUP:
			#다다다다다다다닥
<<<<<<< HEAD
			
=======

		passengerSearch = oodEv_final.passengerSearch(passenger_list,clock)
>>>>>>> e413017a78e66348bc89cea870d35e2d581cc9f5
		passengerIndex = oodEv_final.passengerSearch(passenger_list,clock)
		passenger = passenger_list[passengerIndex]



		passengerIndex = oodEv_final.passengerSearch(passenger_list,clock)
		passenger = passenger_list[passengerIndex]

		ins_n1 = oodEv_final.Elevator()
		ins_n2 = oodEv_final.Elevator()
		ins_n3 = oodEv_final.Elevator()

		if passenger_list != -1:
			oodEv_final.evCall(ins_n1,ins_n2,ins_n3,passenger)

		ins_n1.move(int(round(pygame.time.get_ticks()/1000)))
		ins_n2.move(int(round(pygame.time.get_ticks()/1000)))
		ins_n3.move(int(round(pygame.time.get_ticks()/1000)))

		n1_y = invertfloor(ins_n1.floor)
		n2_y = invertfloor(ins_n2.floor)
		n3_y = invertfloor(ins_n3.floor)
		# n1_y = invertfloor(ins_n1.floor)
		#passanger_list(time, weight, departure, arrival)
		


		o1 = {'rect':pygame.Rect(10,o1_y,elevator_height,elevator_width)}
		o2 = {'rect':pygame.Rect(40,o2_y,elevator_height,elevator_width)}
		o3 = {'rect':pygame.Rect(70,o3_y,elevator_height,elevator_width)}
		Oldboxes =[o1,o2,o3]
		for b1 in Oldboxes:
			pygame.draw.rect(gamePad, RED, b1['rect'])



		n1 = {'rect':pygame.Rect(380,n1_y,elevator_height,elevator_width)}
		n2 = {'rect':pygame.Rect(410,n2_y,elevator_height,elevator_width)}
		n3 = {'rect':pygame.Rect(440,n3_y,elevator_height,elevator_width)}
		Newboxes =[n1,n2,n3]
		for b2 in Newboxes:
			pygame.draw.rect(gamePad,RED,b2['rect'])

#그리는 부분
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
		# elev_info(ev1.listToAdd, 글자 출력 y 축)
		# elev_info(ev2.listToAdd, 글자 출력 y 축)
		# elev_info(ev3.listToAdd, 글자 출력 y 축)

		pygame.draw.line(gamePad, BLACK, (150,390),(300,390),1)
		dispMessage('Throughput = ', 400)
			#기욱씨 임시 인스턴스의 경우 소욧시간변수(=tempEV1,tempEV2,tempEV3)
			#영준형 임시 인스턴스의 경우 소욧시간변수(=)
		# Throughput = passenger_count * arrivaltime_all / 설정time
		# dispMessage(Throughput, 410)

		pygame.display.update()
		# 메인 루프 안에서 FPS(초당 프레임수)를 맞추기 위한 딜레이를 추가해주는 코드. 파라미터로 딜레이 시간이 아닌 목표로 하는 FPS 값이 들어간다.
		clock.tick(TARGET_FPS)
	pygame.quit()
	quit()


def initGame():
	global clock, gamePad,elevator
	pygame.init()
	gamePad = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption(CAPTION)
<<<<<<< HEAD
=======



>>>>>>> e413017a78e66348bc89cea870d35e2d581cc9f5
	rungame()


if __name__=='__main__':
	initGame()
