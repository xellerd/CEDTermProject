# -*- coding: utf-8 -*-

import copy
import random

UP = 1
STOP = 0
DOWN = -1
MOVINGTIME = 3
STOPTIME = 5
MAXLOAD = 20
MAXFLOOR = 12
OPEN = 1
CLOSE = 0
TMAX = 40
RANDTIMEMAX = 30
RANDPASSENGERMAX = 5

class Passenger:
    time = 0
    weight = 0
    departure = 0
    arrival = 0

    def __init__(self, time, weight, departure, arrival):
        self.time = time
        self.weight = weight
        self.departure = departure
        self.arrival = arrival
    def __repr__(self):
        return 'Passenger(time="{0!r}", weight="{1!r}", departure="{2!r}", arrival="{3!r}")'.format(self.time, self.weight, self.departure, self.arrival)

class Destination:
    floor = 0
    weight = 0
    time = 0

    def __init__(self, floor, weight, time):
        self.floor = floor
        self.weight = weight
        self.time = time

    def __repr__(self):
        return 'Destination(floor="{0!r}", weight="{1!r}", time="{2!r}")\n'.format(self.floor, self.weight, self.time)
    def keyfunc1(c):
        return c.floor
    def keyfunc2(c):
        return c.weight
    def keyfunc3(c):
        return c.time

class Elevator:
    weight = 0
    direction = STOP
    door = CLOSE
    destUp = []
    destDown = []
    destAdd = []
    dest = []
    floor = 1
    time = 0

    def __repr__(self):
        return 'Elevator(\nweight="{0!r}"\ndirection="{1!r}"\ndoor="{2!r}"\ndestUp="{3!r}"\ndestDown="{4!r}"\ndestAdd="{5!r}"\ndest="{6!r}\nfloor="{7!r}"\ntime="{8!r}")'.format(self.weight, self.direction, self.door, self.destUp, self.destDown, self.destAdd, self.dest, self.floor, self.time)

    def move(self, time):
        if self.direction == UP and self.destUp == [] and self.destAdd != []:
            self.destUp = self.destAdd[:]
            self.destAdd = []
        if self.direction == DOWN and self.destDown == [] and self.destAdd != []:
            self.destDown = self.destAdd[:]
            self.destAdd = []

        if self.dest == []:
            self.direction = STOP
        else:
            if self.floor == self.dest[0].floor:
                self.arrive()
                self.door = OPEN
            else:
                self.direction = (self.dest[0].floor-self.floor)/abs(self.dest[0].floor-self.floor)
                int(self.direction)

        if self.door == OPEN:
            if (time - self.time) == STOPTIME:
                self.time = time - MOVINGTIME
                self.door = CLOSE
            else:
                return

        if self.direction == STOP:
            self.door = CLOSE
            self.time = time + 1
        else:
            if (time - self.time) == MOVINGTIME:
                if self.direction == UP:
                    self.floor = self.floor + 1
                elif self.direction == DOWN:
                    self.floor = self.floor - 1
                self.time = time
                if self.floor == self.dest[0].floor:
                    self.arrive()
                    self.door = OPEN
            else:
                return

    def arrive(self):
        self.weight = self.weight + self.dest[0].weight
        a = self.dest.pop(0)

        if self.direction == UP:
            self.destUp.pop(0)
        elif self.direction == DOWN:
            self.destDown.pop(0)

        while True:
            if self.dest[0].floor == a.floor:
                self.weight = self.weight + self.dest[0].weight
                a = self.dest.pop(0)

                if self.direction == UP:
                    self.destUp.pop(0)
                elif self.direction == DOWN:
                    self.destDown.pop(0)
            else:
                break

    def addDest(self, passenger):
        print("addDest!")
        print(id(self))
        departure = Destination(passenger.departure, passenger.weight, passenger.time)
        arrival = Destination(passenger.arrival, -passenger.weight, passenger.time)

        destDir = (arrival.floor - departure.floor) / abs(arrival.floor - departure.floor)
        int(destDir)

        if self.direction == STOP:
            if destDir == UP:
                if self.floor == departure.floor:
                    # print("case 1")
                    self.destUp.append(arrival)
                    self.dest.append(departure)
                    self.dest = self.dest + self.destUp
                elif self.floor < departure.floor:
                    # print("case 2")
                    self.destUp.append(departure)
                    self.destUp.append(arrival)
                    self.dest = self.dest + self.destUp
                elif self.floor > departure.floor:
                    # print("case 3")
                    self.destDown.append(departure)
                    self.destUp.append(arrival)
                    self.dest = self.destDown + self.destUp
            elif destDir == DOWN:
                if self.floor == departure.floor:
                    # print("case 4")
                    self.destDown.append(arrival)
                    self.dest.append(departure)
                    self.dest = self.dest + self.destDown
                elif self.floor > departure.floor:
                    # print("case 5")
                    self.destDown.append(departure)
                    self.destDown.append(arrival)
                    self.dest = self.dest + self.destDown
                elif self.floor < departure.floor:
                    # print("case 6")
                    self.destUp.append(departure)
                    self.destDown.append(arrival)
                    self.dest = self.destUp + self.destDown
        elif self.direction == UP:
            if destDir == UP:
                if self.floor <= departure.floor:
                    # print("case 7")
                    self.destUp.append(departure)
                    self.destUp.append(arrival)
                    self.destUp.sort(key=Destination.keyfunc1)
                    self.dest = self.destUp + self.destDown + self.destAdd
                elif self.floor > departure.floor:
                    # print("case 8")
                    self.destAdd.append(departure)
                    self.destAdd.append(arrival)
                    self.dest = self.destUp + self.destDown + self.destAdd
            elif destDir == DOWN:
                # print("case 9")
                self.destDown.append(departure)
                self.destDown.append(arrival)
                self.destDown.sort(key=Destination.keyfunc1)
                self.destDown.reverse()
                self.dest = self.destUp + self.destDown + self.destAdd
        elif self.direction == DOWN:
            if destDir == DOWN:
                if self.floor >= departure.floor:
                    # print("case 10")
                    self.destDown.append(departure)
                    self.destDown.append(arrival)
                    self.destDown.sort(key=Destination.keyfunc1)
                    self.destDown.reverse()
                    self.dest = self.destDown + self.destUp + self.destAdd
                elif self.floor < departure.floor:
                    # print("case 11")
                    self.destAdd.append(departure)
                    self.destAdd.append(arrival)
                    self.dest = self.destUp + self.destDown + self.destAdd
            elif destDir == UP:
                # print("case 12")
                self.destUp.append(departure)
                self.destUp.append(arrival)
                self.destUp.sort(key=Destination.keyfunc1)
                self.dest = self.destDown + self.destUp + self.destAdd

    def totalTime(self):
        time = 0
        for destination in self.dest:
            time = time + abs(self.floor - destination.floor)
        return time

def elevatorCall(elevatorList, passenger):
    timeList = []
    for elevator in elevatorList:
        dcpElevator = copy.deepcopy(elevator)
        dcpElevator.addDest(passenger)
        timeList.append(dcpElevator.totalTime())

    idx = timeList.index(min(timeList))
    # print("idx : {0}".format(idx))
    elevatorList[0].addDest(passenger)

def passengerSearch(passengerList, time):
    for passenger in passengerList:
        if passenger.time == time:
            return passenger
    return None

def passengerGenerator(passengerNum):
    timeList = []

    for i in range(passengerNum):
        while True:
            randTime = random.randint(1, RANDTIMEMAX)
            if randTime not in timeList:
                break
        timeList.append(randTime)
    timeList.sort()

    passengerList = []
    for i in range(passengerNum):
        a = random.randint(1, RANDPASSENGERMAX)
        while True:
            b = random.randint(1, MAXFLOOR)
            c = random.randint(1, MAXFLOOR)
            if b != c:
                break
        passenger = Passenger(timeList[i], a, b, c)
        passengerList.append(passenger)
    return passengerList

if __name__ == '__main__':

    t = 0
    passengerNum = 5
    elevatorNum = 3
    ev1=Elevator()
    ev2=Elevator()
    ev3=Elevator()
    elevatorList = [ev1,ev2,ev3]
   


    # print(len(elevatorList))

    while t <= TMAX:
        print("t : %d" % t)
        passengerList = passengerGenerator(passengerNum)

        passenger = passengerSearch(passengerList, t)
        if passenger != None:
            elevatorCall(elevatorList, passenger)


            ev1.move(t)
            ev2.move(t)
            ev3.move(t)

        for elevator in elevatorList:
            print(id(elevator))
            print(elevator)
            print("\n")

        print("\n\n")

        t = t + 1
