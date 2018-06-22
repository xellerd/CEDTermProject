# -*- coding:utf-8 -*-

import random

MOVINGTIME = 3
STOPTIME = 5
MAXLOAD = 20
MAXFLOOR = 12
TMAX = 30
UP = 1
STOP = 0
DOWN = -1

#각 층별 호출발생 확률값
upProblist = [0.8, 0.75, 0.3, 0.4, 0.6, 0.45, 0.5, 0.2, 0.2, 0.1, 0.05, 0]
downProblist = upProblist.reverse()


class user:

	arrivalTime = 0
	def __init__(self):
		self.time = 0
		self.userNum = random.randint(1, 3) #탑승인원
		self.start = random.randint(1, 12) #시작층
		self.destination = random.randint(1, 12) #목적층
		#호출 방향
		if self.destination - self.start > 0:
			self.wantDirect = 1
		elif self.destination - self.start < 0:
			self.wantDirect = -1






class elevator:
	global elv1Passengerlist, elv2Passengerlist, elv3Passengerlist

	def __init__(self):
		self.elevaDirect = random.randint(-1, 1) #-1는 아래로, 0은 정지, 1은 위로 움직이고 있는 상태
		self.passenger = random.randint(1, 3) #현재 탑승하고 있는 인원수
		self.presentFloor = random.randint(1, 12) #현재 위치
		self.time = 0


	def callmove(self, time, elevatorObj, userObj):
		if elevatorObj == elevator1:
			elv1Passengerlist.append(userObj.start)
			if (elevatorObj.elevaDirect == 1) or (elevatorObj.elevaDirect == 0):
				elv1Passengerlist.sort()

			elif elevatorObj.elevaDirect == -1:
				elv1Passengerlist.sort()
				elv1Passengerlist.reverse()

			if elevatorObj.presentFloor == elv1Passengerlist[0]:
				time += STOPTIME
				elv1Passengerlist.pop(0)
				if elv1Passengerlist[0] > elevatorObj.presentFloor:
					elevatorObj.elevaDirect = 1
				elif elv1Passengerlist[0] < elevatorObj.presentFloor:
					elevatorObj.elevaDirect = -1
				elif elv1Passengerlist == []:
					elevatorObj.elevaDirect = 0

			else:
				if (time - elevatorObj.time) == MOVINGTIME:
					elevatorObj.presentFloor = elevatorObj.presentFloor + elevatorObj.elevaDirect
					if elevatorObj.presentFloor == 0 or elevatorObj.presentFloor == 13:
						elevatorObj.presentFloor = elevatorObj.presentFloor - elevatorObj.elevaDirect*2
					elevatorObj.time = time
				else:
					pass

		elif elevatorObj == elevator2:
			elv2Passengerlist.append(userObj.start)
			if (elevatorObj.elevaDirect == 1) or (elevatorObj.elevaDirect == 0):
				elv2Passengerlist.sort()

			elif elevatorObj.elevaDirect == -1:
				elv2Passengerlist.sort()
				elv2Passengerlist.reverse()

			if elevatorObj.presentFloor == elv2Passengerlist[0]:
				time += STOPTIME
				elv2Passengerlist.pop(0)
				if elv2Passengerlist[0] > elevatorObj.presentFloor:
					elevatorObj.elevaDirect = 1
				elif elv2Passengerlist[0] < elevatorObj.presentFloor:
					elevatorObj.elevaDirect = -1
				elif elv2Passengerlist == []:
					elevatorObj.elevaDirect = 0

			else:
				if (time - elevatorObj.time) == MOVINGTIME:
					elevatorObj.presentFloor = elevatorObj.presentFloor + elevatorObj.elevaDirect
					if elevatorObj.presentFloor == 0 or elevatorObj.presentFloor == 13:
						elevatorObj.presentFloor = elevatorObj.presentFloor - elevatorObj.elevaDirect*2
					elevatorObj.time = time
				else:
					pass

		elif elevatorObj == elevator3:
			elv3Passengerlist.append(userObj.start)
			if (elevatorObj.elevaDirect == 1) or (elevatorObj.elevaDirect == 0):
				elv3Passengerlist.sort()

			elif elevatorObj.elevaDirect == -1:
				elv3Passengerlist.sort()
				elv3Passengerlist.reverse()

			if elevatorObj.presentFloor == elv3Passengerlist[0]:
				time += STOPTIME
				elv3Passengerlist.pop(0)
				if elv3Passengerlist[0] > elevatorObj.presentFloor:
					elevatorObj.elevaDirect = 1
				elif elv3Passengerlist[0] < elevatorObj.presentFloor:
					elevatorObj.elevaDirect = -1
				elif elv3Passengerlist == []:
					elevatorObj.elevaDirect = 0

			else:
				if (time - elevatorObj.time) == MOVINGTIME:
					elevatorObj.presentFloor = elevatorObj.presentFloor + elevatorObj.elevaDirect
					if elevatorObj.presentFloor == 0 or elevatorObj.presentFloor == 13:
						elevatorObj.presentFloor = elevatorObj.presentFloor - elevatorObj.elevaDirect*2
					elevatorObj.time = time
				else:
					pass


	def move1(self, time, elevator):
		if elevator.presentFloor == elv1Passengerlist[0]:
			time += STOPTIME
			elv1Passengerlist.pop(0)
			if elv1Passengerlist == []:
				elevator.elevaDirect = 0
			else:
				if elv1Passengerlist[0] > elevator.presentFloor:
					elevator.elevaDirect = 1
				elif elv1Passengerlist[0] < elevator.presentFloor:
					elevator.elevaDirect = -1


		else:
			if (time - elevator.time) == MOVINGTIME:
				elevator.presentFloor = elevator.presentFloor + elevator.elevaDirect
				if elevator.presentFloor == 0 or elevator.presentFloor == 13:
					elevator.presentFloor = elevator.presentFloor - elevator.elevaDirect*2
				elevator.time = time
			else:
				pass


	def move2(self, time, elevator):
		if elevator.presentFloor == elv2Passengerlist[0]:
			time += STOPTIME
			elv2Passengerlist.pop(0)
			if elv2Passengerlist == []:
				elevator.elevaDirect = 0
			else:
				if elv2Passengerlist[0] > elevator.presentFloor:
					elevator.elevaDirect = 1
				elif elv2Passengerlist[0] < elevator.presentFloor:
					elevator.elevaDirect = -1


		else:
			if (time - elevator.time) == MOVINGTIME:
				elevator.presentFloor = elevator.presentFloor + elevator.elevaDirect
				if elevator.presentFloor == 0 or elevator.presentFloor == 13:
					elevator.presentFloor = elevator.presentFloor - elevator.elevaDirect*2
				elevator.time = time
			else:
				pass


	def move3(self, time, elevator):
		if elevator.presentFloor == elv3Passengerlist[0]:
			time += STOPTIME
			elv3Passengerlist.pop(0)
			if elv3Passengerlist == []:
				elevator.elevaDirect = 0
			else:
				if elv3Passengerlist[0] > elevator.presentFloor:
					elevator.elevaDirect = 1
				elif elv3Passengerlist[0] < elevator.presentFloor:
					elevator.elevaDirect = -1


		else:
			if (time - elevator.time) == MOVINGTIME:
				elevator.presentFloor = elevator.presentFloor + elevator.elevaDirect
				if elevator.presentFloor == 0 or elevator.presentFloor == 13:
					elevator.presentFloor = elevator.presentFloor - elevator.elevaDirect*2
				elevator.time = time
			else:
				pass






def call(userObj, elevator1, elevator2, elevator3):
	global total1, total2, total3
	count1 = 0
	count2 = 0
	count3 = 0
	total1 = 0
	total2 = 0
	total3 = 0

	if userObj.wantDirect == elevator1.elevaDirect:
		for i in elv1Passengerlist:
			if ((i > userObj.start) & (i < elevator1.presentFloor)) or ((i < userObj.start) & (i > elevator1.presentFloor)):
				count1 += 1

		total1 = count1*STOPTIME + (abs(elevator1.presentFloor - userObj.start)-count1)*MOVINGTIME


	elif userObj.wantDirect == elevator2.elevaDirect:
		for i in elv2Passengerlist:
			if ((i > userObj.start) & (i < elevator2.presentFloor)) or ((i < userObj.start) & (i > elevator2.presentFloor)):
				count2 += 1

		total2 = count2*STOPTIME + (abs(elevator2.presentFloor - userObj.start)-count2)*MOVINGTIME


	elif userObj.wantDirect == elevator3.elevaDirect:
		for i in elv3Passengerlist:
			if ((i > userObj.start) & (i < elevator3.presentFloor)) or ((i < userObj.start) & (i > elevator3.presentFloor)):
				count3 += 1

		total3 = count3*STOPTIME + (abs(elevator3.presentFloor - userObj.start)-count3)*MOVINGTIME


	if min([total1, total2, total3]) == total1:
		return elevator1

	elif min([total1, total2, total3]) == total2:
		return elevator2

	elif min([total1, total2, total3]) == total3:
		return elevator3




#유저에게 호출시간 부여하는 함수
def useraddtime(userlist, timelist):
    for i in range(len(userlist)):
    	userlist[i].time = timelist[i]
    return userlist

#유저에게 인덱스 부여하는 함수
def userSearch(userlist, time):
    for i in range(len(userlist)):
        if userlist[i].time == time:
            return i

    return -1


#user객체 10명 생성
userlist = list()
for i in range(1, 11):
	u = user()
	userlist.append(u)

#timelist를 유저수만큼 랜덤하게 생성
timelist = [1]
time_num = random.randint(1, 30)
for i in range(9):
	while time_num in timelist:
		time_num = random.randint(1, 30)
	timelist.append(time_num)
timelist.sort()

#각 유저객체에 호출랜덤타임을 설정
userlist = useraddtime(userlist, timelist)


#elevator객체 3개 생성
elevator1 = elevator()
elevator2 = elevator()
elevator3 = elevator()

#각 엘리베이터에 임의의 초기 목적층을 설정해줌
elv1Passengerlist = list()
elv1Passengerlist.append(random.randint(1, 12))
elv2Passengerlist = list()
elv2Passengerlist.append(random.randint(1, 12))
elv3Passengerlist = list()
elv3Passengerlist.append(random.randint(1, 12))



t = 0
while t <= TMAX:
	print("t : %d" %t)

	#현 시간에 해당하는 특정유저 확인_1
	userIndex = userSearch(userlist, t)


	#호출됐을 때의 내용 들어갈 부분
	if userIndex != -1:
		#현 시간에 해당하는 특정유저 확인_2
		userObj = userlist[userIndex]
		#호출로 인해 배차된 특정 엘리베이터 확인
		elevatorObj = call(userObj, elevator1, elevator2, elevator3)

		#엘리베이터 상태 업데이트
		if elevatorObj == elevator1:
			elevator1.callmove(t, elevator1, userObj)
			elevator2.move2(t, elevator2)
			elevator3.move3(t, elevator3)
		elif elevatorObj == elevator2:
			elevator1.move1(t, elevator1)
			elevator2.callmove(t, elevator2, userObj)
			elevator3.move3(t, elevator3)
		elif elevatorObj == elevator3:
			elevator1.move1(t, elevator1)
			elevator2.move2(t, elevator2)
			elevator3.callmove(t, elevator3, userObj)

	#호출되지 않았을 때의 엘리베이터 상태 업데이트
	else:
		elevator1.move1(t, elevator1)
		elevator2.move2(t, elevator2)
		elevator3.move3(t, elevator3)

	print(elevator1.presentFloor)
	print(elevator1.passenger)
	print(elevator2.presentFloor)
	print(elevator3.presentFloor)


	t = t + 1
