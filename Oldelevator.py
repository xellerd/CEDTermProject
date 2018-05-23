class Oldelevator:
def __init__(self, num, passanger, direction, elevelocation) #엘리베이터 이름, 승객수, 방향, 현 위치

	self.num = num
	self.passanger = 0
	self.direction = None
	self.elevlocation = elevlocation


#엘리베이터 사용자가 누른 방향
def call(self,floor,direction):
	if direction not in (1,-1):
		print("1,-1이외의 방향 없음.")
	elif direction = 1:
		if elev.direction = 1:
			println("")
		else:
	if self.floors[floor]:
    elevator = self.choose_elevator(self.floors[floor], direction)
    elevator.open()
    return elevator

	else:
		if elev.direction = -1:

		else:






def take():

def getoff():












def move(self, system):
	system.floors[self.floor].remove(self)
    self.floor += self.direction
    system.floors[self.floor].append(self)
    print("현 층수는{}",self.elevelocation)#엘리베이터 이동방향에 맞게 +1층 -1층



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