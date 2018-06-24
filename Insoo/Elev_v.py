import pygame
import sys
from time import sleep
import time
from pygame.locals import*
import Old_final
import NEWFINALLLL
import random

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
	global clock, gamePad
	gamePad.fill(WHITE)
	
	#OLD_ELEVATOR 객체생성
	ins_o1 = Old_final.elevator()
	ins_o2 = Old_final.elevator()
	ins_o3 = Old_final.elevator()
	#NEW_ELEVATOR 객체생성
	ins_n1 = NEWFINALLLL.Elevator()
	ins_n2 = NEWFINALLLL.Elevator()
	ins_n3 = NEWFINALLLL.Elevator()


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
		# if t != passenger arrivaltime :
		# 	passengerdata = ("call time:"+"%d\t" + "call floor:"+"%d\t"+"destination:"+"%d\t",time,departure,destination)
		

		#화면을 하얀색으로 채워줌으로써 반복되는 것 삭제
		gamePad.fill(WHITE)

		#인터페이스
		drawClock(t)
		dispMessage('passenger_info',20)
		#passanger info : passenger 수 ,호출 층, 목적층, 배차된 엘리베이터
		# passengerMessage = "passenger : %d\t passenger floor : %d\t destination : %d\n Dispatch Old:%d\n Dispatch New:%d"%()

		#타이틀 
		dispMessage('o1 ,n1',80)
		dispMessage('o2 ,n2',170)
		dispMessage('o3 ,n3',260)

		##객체생성 test>>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>.
		# userlist = list()
		# for i in range(1, 11):
		# 	u = Old_final.user()
		# 	userlist.append(u)

		# #timelist를 유저수만큼 랜덤하게 생성
		# timelist = [1]
		# time_num = random.randint(1, 30)
		# for i in range(9):
		# 	while time_num in timelist:
		# 		time_num = random.randint(1, 30)
		# 	timelist.append(time_num)
		# timelist.sort()

		# #각 유저객체에 호출랜덤타임을 설정
		# userlist = Old_final.useraddtime(userlist, timelist)
		# # dispMessage(ins_o3.passenger,100)
		# userIndex = Old_final.userSearch(userlist, t)
		# if userIndex != -1:
		# #현 시간에 해당하는 특정유저 확인_2
		# 	userObj = userlist[userIndex]
		# 	#호출로 인해 배차된 특정 엘리베이터 확인
		# 	elevatorObj = Old_final.call(userObj, ins_o1, ins_o2, ins_o3)
		# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		floor_end=[400,370,340,310,280,250,220,190,160,130,100,70]
		for h in floor_end:	
			pygame.draw.line(gamePad, BLACK, (0,h),(100,h),1)
			pygame.draw.line(gamePad, BLACK, (360,h),(450,h),1)
		pygame.draw.line(gamePad, BLACK, (100,10),(100,490),3)
		pygame.draw.line(gamePad, BLACK, (360,10),(360,490),3)
		pygame.draw.line(gamePad, BLACK, (150,390),(300,390),1)
		dispMessage('Throughput = ', 400)
		

		#OLD_ELEVATOR
		ins_o1.move1(int(round(pygame.time.get_ticks()/1000)),ins_o1)
		ins_o2.move2(int(round(pygame.time.get_ticks()/1000)),ins_o2)
		ins_o3.move3(int(round(pygame.time.get_ticks()/1000)),ins_o3)
		o1_y = invertfloor(ins_o1.presentFloor)
		o2_y = invertfloor(ins_o2.presentFloor)
		o3_y = invertfloor(ins_o3.presentFloor)
		o1 = pygame.Rect(10,o1_y, elevator_height, elevator_width)
		o2 = pygame.Rect(40,o2_y,elevator_height,elevator_width)
		o3 = pygame.Rect(70,o3_y,elevator_height,elevator_width)
		pygame.draw.rect(gamePad,RED,o1,0)
		pygame.draw.rect(gamePad,RED,o2,0)
		pygame.draw.rect(gamePad,RED,o3,0)


		#NEW_ELEVATOR
		passengerNum = 10
		elevatorList = [ins_n1,ins_n2,ins_n3]
		passengerListt = NEWFINALLLL.passengerGenerator(passengerNum)
		passengerr = NEWFINALLLL.passengerSearch(passengerListt, t)
		if passengerr != None:
			NEWFINALLLL.elevatorCall(elevatorList, passengerr)
			print()

		ins_n1.move(int(round(pygame.time.get_ticks()/1000)))
		ins_n2.move(int(round(pygame.time.get_ticks()/1000)))
		ins_n3.move(int(round(pygame.time.get_ticks()/1000)))
		n1 = pygame.Rect(370,invertfloor(ins_n1.floor),elevator_height,elevator_width)
		n2 = pygame.Rect(400,invertfloor(ins_n2.floor),elevator_height,elevator_width)
		n3 = pygame.Rect(430,invertfloor(ins_n3.floor),elevator_height,elevator_width)
		pygame.draw.rect(gamePad,RED,n1,0)
		pygame.draw.rect(gamePad,RED,n2,0)
		pygame.draw.rect(gamePad,RED,n3,0)


		

		data_o1 = "old[1] :passenger:%d \t floor:%d" %(ins_o1.passenger,ins_o1.presentFloor)
		data_o2 = "old[2] :passenger:%d \t floor:%d" %(ins_o2.passenger,ins_o2.presentFloor)
		data_o3 = "old[3] :passenger:%d \t floor:%d" %(ins_o3.passenger,ins_o3.presentFloor)

		data_n1 = "new[1] :passenger:%d \t floor:%d" %(ins_n1.weight,ins_n1.floor)
		data_n2 = "new[2] :passenger:%d \t floor:%d" %(ins_n2.weight,ins_n2.floor)
		data_n3 = "new[3] :passenger:%d \t floor:%d" %(ins_n3.weight,ins_n3.floor)
		dispMessage(data_o1,100)
		dispMessage(data_o2,190)
		dispMessage(data_o3,280)
		dispMessage(data_n1,115)
		dispMessage(data_n2,205)
		dispMessage(data_n3,295)

		# Throughput = str((ins_o1.objCount1+ins_o2.objCount2+ins_o3.objCount3)/t)
		# dispMessage(Throughput,410)
		t = t+1
		print(t)
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