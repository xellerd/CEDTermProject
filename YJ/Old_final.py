import random

class user:
	def __init__(self):
		self.userNum = random.randint(1, 2) #탑승인원
		self.destination = random.randint(1, 12) #목적층
		self.start = random.randint(1, 12) #시작층
		self.select = random.randint(1, 3) #어떤 엘리베이터 라인의 버튼을 눌렀는가
		self.wantDirect = destination - start #가고자하는 방향



class elevator:
	def __init__(self):
		self.elevaDirect = random.randint(1, 2) #1은 위로, 2는 아래로 움직이고 있는 상태
		self.passenger = random.randint(1, 3) #현재 탑승하고 있는 인원수
		self.presentFloor = random.randint(1, 12) #현재 위치 
		


class system:
	def __init__(self):
		pass

#user객체 10명 생성
for i in range(1, 10):
	user"%d" = user() %i

#elevator객체 3개 생성
for i in range(1, 3):
	elevator"%d" = elevator() %i 