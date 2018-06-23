import pygame
import sys
from time import sleep
import time
from pygame.locals import*
<<<<<<< HEAD:Insoo/sadfinal.py
import oodEv_final
=======
>>>>>>> c8b68aa47cbed121c4113ec11d835e43aeef07dd:YJ/sadfinal.py
import Old_final

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
	largeText = pygame.font.Font('freesansbold.ttf',10)
	TextSurf, TextRect = textObject(text,largeText)
	TextRect.center = (225,y)
	gamePad.blit(TextSurf, TextRect)

	pygame.display.update()

def drawClock(count):
	global gamePad, clockcount
	
	font = pygame.font.Font('freesansbold.ttf', 10)
	text = font.render('Clock:'+str(count),True,BLACK)
	gamePad.blit(text,(0,0))

def invertfloor(floor):
	floor = 400-30*(floor-1)
	return floor
def move(self, vect):
    x = self.x
    y = vect[1] - self.rect.top

    self.rect.move_ip(x, y)



def rungame():
	global clock, gamePad,passengerList

	clock_count=0
	gamePad.fill(WHITE)
	
<<<<<<< HEAD:Insoo/sadfinal.py
	# ins_o1 = Old_final.elevator()
	# ins_o2 = Old_final.elevator()
	# ins_o3 = Old_final.elevator()

	ins_o1 = Old_final.elevator()
	ins_o2 = Old_final.elevator()
	ins_o3 = Old_final.elevator()
	
	ins_n1 = oodEv_final.Elevator()
	ins_n2 = oodEv_final.Elevator()
	ins_n3 = oodEv_final.Elevator()

=======
	ins_n1 = Old_final.elevator1
	ins_n2 = Old_final.elevator2
	ins_n3 = Old_final.elevator3
	
>>>>>>> c8b68aa47cbed121c4113ec11d835e43aeef07dd:YJ/sadfinal.py

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
#엘리베이터의 위치를 불러온다 엘리베이터 현 위치값 
		
#엘리베이터의 위치를 불러온다 엘리베이터 현 위치값 
		# ins_o1.call()


		ins_o1.move1(int(round(pygame.time.get_ticks()/1000)),ins_o1)
		ins_o2.move2(int(round(pygame.time.get_ticks()/1000)),ins_o2)
		ins_o3.move3(int(round(pygame.time.get_ticks()/1000)),ins_o3)
		o1_y = invertfloor(ins_o1.presentFloor)
		x = 40
		o1 = pygame.Rect(x,o1_y,elevator_height,elevator_width)

<<<<<<< HEAD:Insoo/sadfinal.py
		o2 = pygame.Rect(40,invertfloor(ins_o2.presentFloor),elevator_height,elevator_width)

		o3 = pygame.Rect(70,invertfloor(ins_o3.presentFloor),elevator_height,elevator_width)
=======
		#passengerList = [oodEv_final.Passenger(1, 2, 3, 6), oodEv_final.Passenger(2,5,7,2)]	
		#passengerIndex = oodEv_final.passengerSearch(passengerList, t)
		#passenger = passengerList[passengerIndex]

		#if userIndex != -1:
		#	Old_final.evCall(ins_n1,ins_n2,ins_n3,passenger)
>>>>>>> c8b68aa47cbed121c4113ec11d835e43aeef07dd:YJ/sadfinal.py

		Oldboxes = [o1,o2,o3]

		# pygame.draw.rect(gamePad,RED,elevator_height,elevator_width)
		print(o1_y)
		pygame.draw.rect(gamePad,RED,o1,0)

		pygame.draw.rect(gamePad,RED,o2,0)
		pygame.draw.rect(gamePad,RED,o3,0)
			

		ins_n1.move1(int(round(pygame.time.get_ticks()/1000)))
		ins_n2.move2(int(round(pygame.time.get_ticks()/1000)))
		ins_n3.move3(int(round(pygame.time.get_ticks()/1000)))

		n1 = pygame.Rect(380,invertfloor(ins_n1.floor),elevator_height,elevator_width)
		n2 = pygame.Rect(410,invertfloor(ins_n2.floor),elevator_height,elevator_width)
		n3 = pygame.Rect(440,invertfloor(ins_n3.floor),elevator_height,elevator_width)

		Newboxes = [n1,n2,n3]
		for i in Newboxes :
			pygame.draw.rect(gamePad,RED,n1,0)
			pygame.draw.rect(gamePad,RED,n2,0)
			pygame.draw.rect(gamePad,RED,n3,0)		

		# Oldboxes =[o1,o2,o3]
		# for b1 in Oldboxes:
		# 	pygame.draw.rect(gamePad, RED, b1['rect'])



		# o1.move(10,invertfloor(ins_o1.presentFloor))
			#data = x 초 ~층에서 ~명이 호출, 
   # 		for i in range(len(passengerList)):
			# data = "%d초\t%d층에서\t%d명이 호출\t\t현재 n1위치: %d" %(passengerList[i].time,passenger[i].departure,passenger[i].weight, ins_n1.floor)
			# if passengerList[0]==t
			# 	dispMessage(data,60)
		# if ins_n1.floor가 바뀐다면 
		# 	dispMessage(data, n1위치)
		# elif ins_n2.floor가 바뀐다면
		# 	dispMessage(data, n2위치)
		# elif ins_n3.floor가 바뀐다면
		# 	dispMessage(data, n3위치)






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