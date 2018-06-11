# Movelist[[floor, destination][F,D],[F,D]]
# 기존 엘리베이터는 분할 호출방식
# - 방향먼저,-> 그다음에 가까운 위치

def Destination(self, destination):
	destination = [self.destination]

def MoveList(self, floor, destination):
	MoveList[self.floors[],self.destination[]] #call 로 완성된 floor 집합과 destination 집합을 모아서 엘리베이터의 실제 MoveList
	#잘 모르겠음
def up_floorlist(self, upfloor):
	upfloorlist=[self.upfloor]
def down_floorlist(self, downfloor):
	downfloorlist=[self.downfloor]

	
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
		#엘리베이터가 내려갈때는 Movelist = Downfloor + destination 더해서 sort //만약 현 상황에서 해결 불가능이라면 -> floor 리스트에 계속해서 저장.
		#엘리베이터가 올라갈때는 Movelist = Upfloor + destination 더해서 sort // 만약 현 상황에서 해결 불가능이라면 -> floor 리스트에 계속해서 저자.
		#엘리베이터 방향이 바뀔 때 Movelist change
		#Special case = 