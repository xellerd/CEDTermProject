import random


class elevator:
	global elv1, elv2, elv3

	def __init__(self, destlist, button, destination):
		self.destlist = destlist #목적지 써진 리스트
		self.button = button
		self.destination = destination


	def move(self, button, destination, start, want, time):
	
	if button == 1:
		if elevator1.floor >= start:
			if (elevator1.direction == 1) & (want == 1):
				#방향이 같으면 엘베가 찍고 오기.
			elif (elevator1.direction == 2) & (want == 1):
				if elv1[0] >= start:
					#먼저 찍고 오기
				elif elv1[0] < start:
			        #찍고 태우러 오기
			elif (elevator1.direction == 1) & (want == 2):
				#먼저 찍고 오기
			elif (elevator1.direction == 2) & (want == 2):
				if elv1[0] >= start:
					#찍고 오기
				elif elv1[0] < start:
					#먼저 태우고 찍기

		elif elevator1.floor < start:
			if (elevator1.direction == 1) & (want == 1):
				if elv1[0] < start:
						#찍고 태우기
				elif elv1[0] >= start:
				#태우고 찍기
			elif (elevator1.direction == 2) & (want == 1):
					#먼저 찍고 오기
			elif (elevator1.direction == 1) & (want == 2):
						#찍고 태우기
			elif (elevator1.direction == 2) & (want == 2):
					#찍고 오기
				


	elif button == 2:
		if elevator1.floor >= start:
			if (elevator1.direction == 1) & (want == 1):
				#방향이 같으면 엘베가 찍고 오기.
			elif (elevator1.direction == 2) & (want == 1):
				if elv1[0] >= start:
					#먼저 찍고 오기
				elif elv1[0] < start:
			        #먼저 태우고 찍기
			elif (elevator1.direction == 1) & (want == 2):
				#먼저 찍고 오기
			elif (elevator1.direction == 2) & (want == 2):
				if elv1[0] >= start:
					#찍고 오기
				elif elv1[0] < start:
					#먼저 태우고 찍기

		elif elevator1.floor < start:
			if (elevator1.direction == 1) & (want == 1):
				if elv1[0] < start:
						#찍고 태우기
				elif elv1[0] >= start:
				#태우고 찍기
			elif (elevator1.direction == 2) & (want == 1):
					#먼저 찍고 오기
			elif (elevator1.direction == 1) & (want == 2):
						#찍고 태우기
			elif (elevator1.direction == 2) & (want == 2):
					#찍고 오기
		


	elif button == 3:
		if elevator1.floor >= start:
			if (elevator1.direction == 1) & (want == 1):
				#방향이 같으면 엘베가 찍고 오기.
			elif (elevator1.direction == 2) & (want == 1):
				if elv1[0] >= start:
					#먼저 찍고 오기
				elif elv1[0] < start:
			        #먼저 태우고 찍기
			elif (elevator1.direction == 1) & (want == 2):
				#먼저 찍고 오기
			elif (elevator1.direction == 2) & (want == 2):
				if elv1[0] >= start:
					#찍고 오기
				elif elv1[0] < start:
					#먼저 태우고 찍기

		elif elevator1.floor < start:
			if (elevator1.direction == 1) & (want == 1):
				if elv1[0] < start:
						#찍고 태우기
				elif elv1[0] >= start:
				#태우고 찍기
			elif (elevator1.direction == 2) & (want == 1):
					#먼저 찍고 오기
			elif (elevator1.direction == 1) & (want == 2):
						#찍고 태우기
			elif (elevator1.direction == 2) & (want == 2):
					#찍고 오기
		




class randomNumber: #난수로 사용자와 엘리베이터 상태정보 설정하는 클래스
	def __init__(self):
		pass

	def userinfo(self):
		userNum = random.randint(1, 2)
		destination = random.randint(1, 10)
		start = random.randint(1, 10)
		button = random.randint(1, 3) #어떤 엘베 라인의 버튼을 호출했는가임
		want = destination - start
		return userNum, destination, start, button, want

	def elevatorinfo(self):
		direction = random.randint(0, 2) #0은 정지, 1은 위, 2는 아래 움직이고 있는 상태
		passenger = random.randint(1, 3)
		floor = random.randint(1, 10)
		return direction, passenger, floor

#승객 3그룹 상태정보
user1 = randomNumber()
user1.userinfo()
user2 = randomNumber()
user2.userinfo()
user3 = randomNumber()
user3.userinfo()
#엘리베이터 3대 상태정보
elevator1 = randomNumber()
elevator1.elevatorinfo()
elevator2 = randomNumber()
elevator2.elevatorinfo()
elevator3 = randomNumber()
elevator3.elevatorinfo()
#엘리베이터 임의의 목적지 하나가 입력된 상태를 나타냄
elv1 = list()
elv1.append(random.randint(1, 10))
elv2 = list()
elv2.append(random.randint(1, 10))
elv3 = list()
elv3.append(random.randint(1, 10))

#timelist를 유저수만큼 랜덤하게 생성 
timelist = list()
time_num = random.randint(1, 10)
for i in range(3):
	while time_num in timelist:
		time_num = random.randint(1, 10)
	timelist.append(time_num)
timelist.sort()


#올라가는 uplist 생성

#내려가는 downlist 생성

#uplist + downlist = destrnationlist


#시간순서에 맞도록 유저가 엘리베이터 호출함
user1.move(user1.button, user1.destination, user1.start, user1.want, timelist[0])
user2.move(user2.button, user2.destination, user2.start, user2.want, timelist[1])
user3.move(user3.button, user3.destination, user3.start, user3.want, timelist[2])

#유저, 엘리베이터, 배치시스템 클래스 따로 만들기




def Destination(self, destination):
	destination = [self.destination]


def ONLIST(self, floor, destination):
	MoveList[self.floors[],self.destination[]] #call 로 완성된 floor 집합과 destination 집합을 모아서 엘리베이터의 실제 MoveList
	#잘 모르겠음
	
def call(self, floor):
calldirection
floor = floors[self.call]



	if elevlocation -floor >0
		if elevDirection == 1:
			if calldirection == up: #엘베가 나보다 위에 있고 엘베가 올라가고 있음 그리고 나도 올라가고 싶음
				floors[].append(self.floor)  
				#모든 destination 찍고 내려오는 #방향이 다시 같아질 때 sort.
				floors[].sort()
			elif calldirection == down:  #엘베가 나보다 위에 있고 엘베가 올라가고 있음 그런데 난 내려가고 싶음
				floors[].append(self.floor)
				floors[].sort()
				if floor == elevlocation:
					floorlist[].remove(self.floor)
			#마지막에 넣어주고 방향이 바뀔때 sort 해준다.

		elif elevDirection == -1:
			if calldirection ==up:
				floor[].append(self.floor)
					
			elif calldirection ==down:
				floors[].append(self.floor)


#elevator가 floor 보다 밑층에 있다. 
	elif elevlocation -floor < 0
		if elevDirection == -1: #elevator가 내려가고 있으면
			if calldirection == up:
			#계속해서 미룬다.
				Movelist[].append()
				if cal
			elif calldirection ==down:
			#계속 미루고 방향이 바뀔때 sort 해준다. 
				Movelist[].append()
				Movelist[].sort()
				Movelist[].reverse()

		elif elevDirection ==1: #엘리베이터 위로 가고 있음.
			Movelist[].append()
		
		#하다보니 결론 :

		
		#UPDestination DOWNDestination
		#Upfloor Downfloor 각각 2개씩 필요 
		#엘리베이터가 내려갈때는 Movelist = Downfloor + DOWNDestination 더해서 sort //만약 현 상황에서 해결 불가능이라면 -> floor 리스트에 계속해서 저장.
		#엘리베이터가 올라갈때는 Movelist = Upfloor + UPDestination 더해서 sort // 만약 현 상황에서 해결 불가능이라면 -> 
		#엘리베이터 방향이 바뀔 때 Movelist change