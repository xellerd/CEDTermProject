class Oldelevator:
	waittime = 5
	uptime=5
	downtime=5
def __init__(self, num, passanger, direction, elevelocation): #엘리베이터 이름, 승객수, 방향, 현 위치

	self.num = num
	self.passanger = 0
	self.direction = None
	self.elevlocation = 0


#call 받은 엘리베이터 이동 명령
def move(self, up, down,stop,wait):
	self. up = elevelocation+1
	self. down = elevelocation-1
	self. stop = None

	while call.destlist[]!=None :
		if elevlocation<floor:
			if call.direction ==1or -1:
				elevlocation.up
				++uptime
				if elevlocation == floor:
					elevlocation.stop
					++waittime
					call.floors[self.floor].remove(self)
		elif elevlocation>floor:
			if call.direction == -1 or 1:
				elevlocation.down
				++downtime
				if elevlocation == floor:
					elevlocation.stop
					++waittime
					call.floors[self.floor].remove(self)

def call(self, floor,destination):
	floor=[1,2,3,4,5,6,7,8,9,10,11,12]
	floors = [self.floor]
	destlist = [self.destination]

	if elevlocation < floor and direction == 1:
			destlist.append(self.destination)
			destlist.sort()
		if floors[] != destlist[] :
			destlist.remove(self.destination)
			destlist
def totaltime():
# 사용자 마다 걸린 시간 + 엘리베이터 이동 시간 / 사용자 수?




def display(self, system):
	if call.destlistination.update():
		print("현 위치는 %d 층 입니다.", )

	print("현재 엘리베이터 위치 <%s층> 입니다.",elevlocation)
    print("방향은 <%d>방향입니다.",direction)#엘리베이터 이동방향에 맞게 +1층 -1층



# def call_elevator(self, floor, direction):
#     self.validate_floor(floor)
#     if direction not in (1, -1):
#         raise ValueError("direction only accepts 1 or -1, not {}".
#                                                         format(direction))

#         #Check if there's any elevators on the current floor
#     if self.floors[floor]:
#         elevator = self.choose_elevator(self.floors[floor], direction)
#         elevator.open()
#         return elevator

#         #Now search outward, one floor up and down at a time.
#         #None pads the list if we run out of floors in one direction
#     check_floors = map(None, range(floor + 1, len(self.floors)),
#                              range(floor - 1, -1, -1))
#     for up, down in check_floors:
#         if down is not None and self.floors[down]:
#             elevator = self.choose_elevator(self.floors[down], direction)
#             break
#         if up is not None and self.floors[up]:
#             elevator = self.choose_elevator(self.floors[up], direction)
#             break
#     else:
#         raise Exception("Cannot find elevators.")
#     self.move_elevator(elevator, floor)
#     return elevator       

# def move_elevator(self, elevator, floor):
#         """Send elevator to floor, moving one floor at a time."""

#  self.validate_floor(floor)
#         print("Elevator {} moving".format(elevator.num))

#         move_up = elevator.floor < floor
#         elevator.direction = 1 if move_up else -1

#         # Build the range based on which direction we need to go
#         # We do this because range won't work if floor < elevator.floor
#         for _ in (range(elevator.floor, floor) if move_up
#                             else range(elevator.floor, floor, -1)):
#             elevator.move(self)
#             sleep(0.5)

#         elevator.open()
#         elevator.direction = None