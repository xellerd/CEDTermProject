class Elevator:
    def __init__(self, passenger, direction, destination1, destination2, elevatorFloor):
        self.passenger = passenger
        self.direction = direction
        self.destination1 = destination1
        self.destination2 = destination2
        self.elevatorFloor = elevatorFloor

    def call(self, direction, floor, destination):
        if direction == 1:
            # if floor not in destination1 and floor not in destination2:
                if floor < elevatorFloor:
                    self.destination1.append(floor)
                    self.destination1.sort()
                elif floor > elevatorFloor:
                    self.destination2.append(floor)
                    self.destination2.sort()
                    self.destination2.reverse()

        elif direction == -1:
            # if floor not in destination1 and floor not in destination2:
            if floor > elevatorFloor:
                self.destination2.append(floor)
                self.destination2.sort()
                self.destination2.reverse()
            elif floor < elevatorFloor:
                self.destination1.append(floor)
                self.destination1.sort()

        #after getting on the elevator

        self.passenger += 2

        if direction == 1:
            # if destination not in destination1:
            self.destination1.append(floor)
            self.destination1.sort()

        if direction == -1:
            # if destination not in destination2:
            self.destination2.append(floor)
            self.destination2.sort()
            self.destination2.reverse()



    def elevatorMove(self):
        if direction == 1:
            #destination1 순서대로 이동
            #destination 도착 시
            self.passenger -= 1 #get on 시 +2와 상쇄되어 +1의 효과, get on이 아닌 destination에서는 get off(-1)

        if direction == -1:
            #destination2 순서대로 이동
            #destination 도착 시
            self.passenger -= 1 #get on 시 +2와 상쇄되어 +1의 효과, get on이 아닌 destination에서는 get off(-1)
