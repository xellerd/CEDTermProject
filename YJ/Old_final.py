import random

MOVINGTIME = 2
STOPTIME = 5
MAXLOAD = 20
MAXFLOOR = 12

#각 층별 호출발생 확률값
upProblist = [0.8, 0.75, 0.3, 0.4, 0.6, 0.45, 0.5, 0.2, 0.2, 0.1, 0.05, 0] 
downProblist = upProblist.reverse()


class user:
	def __init__(self):
		self.userNum = random.randint(1, 2) #탑승인원
		self.destination = random.randint(1, 12) #목적층
		self.start = random.randint(1, 12) #시작층
		#호출 방향
		if destination - start > 0:
			self.wantDirect = 1
		elif destination - start < 0:
			self.wantDirect = 2
		



class elevator:
	global elv1Passengerlist, elv2Passengerlist, elv3Passengerlist, userlist, elevatorlist

	def __init__(self):
		#엘리베이터 방향 , 현재 위치랑 현재 목적층 가지고 설정해야함
		self.elevaDirect = random.randint(0, 2) #0은 정지, 1은 위로, 2는 아래로 움직이고 있는 상태
		self.passenger = random.randint(1, 3) #현재 탑승하고 있는 인원수
		self.presentFloor = random.randint(1, 12) #현재 위치 
		

	def call(self, wantDirect, start, destination):
		count1 = 0
		count2 = 0
		count3 = 0

		if wantDirect == elevatorlist[0].elevaDirect:
			for i in elv1Passengerlist:
				if ((i > start) & (i < elevatorlist[0].presentFloor)) or ((i < start) & (i > elevatorlist[0].presentFloor)):
				count1 += 1 

			total1 = count1*STOPTIME + (abs(elevatorlist[0].presentFloor - start)-count1)*MOVINGTIME


		if wantDirect == elevatorlist[1].elevaDirect:
			for i in elv2Passengerlist:
				if ((i > start) & (i < elevatorlist[1].presentFloor)) or ((i < start) & (i > elevatorlist[1].presentFloor)):
				count2 += 1 

			total2 = count2*STOPTIME + (abs(elevatorlist[1].presentFloor - start)-count2)*MOVINGTIME


		if wantDirect == elevatorlist[2].elevaDirect:
			for i in elv3Passengerlist:
				if ((i > start) & (i < elevatorlist[2].presentFloor)) or ((i < start) & (i > elevatorlist[2].presentFloor)):
				count3 += 1 

			total3 = count3*STOPTIME + (abs(elevatorlist[2].presentFloor - start)-count3)*MOVINGTIME

		if min([total1, total2, total3]) == total1:
			elv1Passengerlist.append(destination)

		elif min([total1, total2, total3]) == total2:
			elv2Passengerlist.append(destination)

		elif min([total1, total2, total3]) == total3:
			elv3Passengerlist.append(destination)


class system:
	def __init__(self):
		pass

#user객체 10명 생성
userlist = list()
for i in range(1, 10):
	user = user()
	userlist.append(user)


#elevator객체 3개 생성
elevatorlist = list()
for i in range(1, 3):
	elevator = elevator()
	elevatorlist.append(elevator) 


#각 엘리베이터에 임의의 초기 목적층을 설정해줌
elv1Passengerlist = list()
elv1Passengerlist.append(random.randint(1, 12))
elv2Passengerlist = list()
elv2Passengerlist.append(random.randint(1, 12))
elv3Passengerlist = list()
elv3Passengerlist.append(random.randint(1, 12))


#timelist를 유저수만큼 랜덤하게 생성 
timelist = list()
time_num = random.randint(1, 50)
for i in range(10):
	while time_num in timelist:
		time_num = random.randint(1, 50)
	timelist.append(time_num)
timelist.sort()


userlist[0].call(userlist[0].wantDirect, userlist[0].start, userlist[0].destination)