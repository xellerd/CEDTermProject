

		#하다보니 결론 :
		#UPDestination DOWNDestination
		#Upfloor Downfloor 각각 2개씩 필요 
		#엘리베이터가 내려갈때는 Movelist = Downfloor + destination 더해서 sort //만약 현 상황에서 해결 불가능이라면 -> floor 리스트에 계속해서 저장.
		#엘리베이터가 올라갈때는 Movelist = Upfloor + destination 더해서 sort // 만약 현 상황에서 해결 불가능이라면 -> floor 리스트에 계속해서 저자.
		#엘리베이터 방향이 바뀔 때 Movelist change
		#Special case = 
class Oldelevator:
	waittime = 5
	uptime=5
	downtime=5
		def __init__(self, num, passanger, direction, elevelocation): #엘리베이터 이름, 승객수, 방향, 현 위치

			self.num = num
			self.passanger = passanger
			self.direction = direction
			self.elevlocation = elevlocation
		def getdestination(self, destination):
			destination[] = input(self. destination) #random값 등록.(나중에)
			while True:
				destination[].append(self.destination)
			print("현 등록 목적층 :" + destination)
		def inner_destination(self, destinations):
			if self.destinations[destination]:
				elevator = self.inner_destination(self.destinations[destination])
				elevator.printinfo()



			if floordirection not in (1 , -1):
				raise ValueError("방향은 1과 -1만 등록")
			else :
			
		def call(self,floor):

			while True:
				if self.floordirection == 1:
					upfloors[].append(self.floor)
					print(floor+": 층에서 호출(upfloor저장)")
				elif self.floordirection == -1:
					downfloors[].append(self.floor)
					print(floor+": 층에서 호출(downfloor저장)")

		def printinfo():
			print("Movelistㅇ 있는 목적층 도착")
				print("현재 위치",elevlocation)
				print("탑승인원",passanger)
				print("내부 눌린 목적층",destinations)
				print("")
		def move():
			while True:
				if Movelist[] != None:
					if direction == 1 : 
						sleep(2)
						elevlocation ++
						

						Movelist[]= upfloor[]+destination[]
						Movelist[].sort()
						if  elevlocation>floor:
							upfloor[].append(floor)

						elif elevlocation in Movelist[]:
							elevlocation = elevlocation
							elevator.printinfo()
							sleep(5)
						else:
							pass
						



					elif direction == -1:
						slee(2)
						elevlocation --
						Movelist[]= downfloor[]+destination[]
						Movelist[].sort()
						if elevlocation<floor:
							downfloor[].append(floor)

						elif elevlocation in Movelist[]:
							elevlocation = elevlocation
							elevator.printinf()
							sleep(5)
						else:
							pass
				elif Movelist[] ==None:
					elevlocation = elevlocation

					
		      #   self.validate_floor(floor)
        # if direction not in (1, -1):
        #     raise ValueError("direction only accepts 1 or -1, not {}".
        #                                                 format(direction))

        # #Check if there's any elevators on the current floor
        # if self.floors[floor]:
        #     elevator = self.choose_elevator(self.floors[floor], direction)
        #     elevator.open()
        #     return elevator

        # #Now search outward, one floor up and down at a time.
        # #None pads the list if we run out of floors in one direction
        # check_floors = map(None, range(floor + 1, len(self.floors)),
        #                          range(floor - 1, -1, -1))
        # for up, down in check_floors:
        #     if down is not None and self.floors[down]:
        #         elevator = self.choose_elevator(self.floors[down], direction)
        #         break
        #     if up is not None and self.floors[up]:
        #         elevator = self.choose_elevator(self.floors[up], direction)
        #         break
        # else:
        #     raise Exception("Cannot find elevators.")

        # self.move_elevator(elevator, floor)
        # return elevator       