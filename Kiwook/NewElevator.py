UP = 1
STOP = 0
DOWN = -1


class Elevator:
    def __init__(self, passenger, direction, destinationUp, destinationDown, destinationList, elevatorFloor):
        self.passenger = passenger
        self.direction = direction
        self.destinationUp = destinationUp
        self.destinationDown = destinationDown
        self.destinationList = destinationList
        self.elevatorFloor = elevatorFloor

    def call(self, floor, destination, number):
        group = [number, destination]
        groupDirection = (destination - floor)/abs(destination - floor)

        if groupDirection == UP:
            self.destinationUp.append(group)
            self.destinationUp.sort()
            if (self.elevatorFloor - floor) < 0 and self.direction != DOWN:
                # self.destinationUp.append(group)
                # self.destinationUp.sort()
                self.destinationList.append(self.destinationUp)
                self.destinationList.append(self.destinationDown)
            elif (self.elevatorFloor - floor) < 0 and self.direction == DOWN:
                # self.destinationUp.append(group)
                # self.destinationUp.sort()
                self.destinationList.append(self.destinationDown)
                self.destinationList.append(self.destinationUp)
        elif groupDirection == DOWN:
            self.destinationDown.append(group)
            self.destinationDown.sort()
            self.destinationDown.reverse()
            if (self.elevatorFloor - floor) > 0 and self.direction != UP:
                # self.destinationDown.append(group)
                # self.destinationDown.sort()
                # self.destinationDown.reverse()
                self.destinationList.append(self.destinationDown)
                self.destinationList.appned(self.destinationUp)
            elif (self.elevatorFloor - floor) > 0 and self.direction == UP:
                # self.destinationDown.appned(group)
                # self.destinationDown.sort()
                # self.destinationDown.reverse()
                self.destinationList.append(self.destinationUp)
                self.destinationList.appned(self.destinationDown)





    def take(self):

    def getOff(self, floor):

    def move:
