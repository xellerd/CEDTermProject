# Movelist[[floor, destination][F,D],[F,D]]
# 기존 엘리베이터는 분할 호출방식
# - 방향먼저,-> 그다음에 가까운 위치

import random


class dispatch:


class elevator:
	def move():



class randomNumber: #난수 발생 클래스
	def __init__(self):
		pass

	def userinfo(self):
		time = random.randint(1,5)
		userNum = random.randint(1, 2)
		destination = random.randint(1, 10)
		start = random.randint(1, 10)
		button = random.randint(1, 3) #어떤 엘베 라인의 버튼을 호출했는가임
		return time, userNum, destination, start, button

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
#엘리베이터 3대 상태 정보
elevator1 = randomNumber()
elevator1.elevatorinfo()
elevator2 = randomNumber()
elevator2.elevatorinfo()
elevator3 = randomNumber()
elevator3.elevatorinfo() 



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