# -*- coding: utf-8 -*-

import copy
import random
#constant
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

class Passenger:  #승객
    time = 0
    weight = 0
    departure = 0
    arrival = 0
    arrivalTime = 0

    def __init__(self, time, weight, departure, arrival):
        self.time = time
        self.weight = weight
        self.departure = departure
        self.arrival = arrival

    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime

class Destination:  #승객 목적지
    floor = 0
    weight = 0
    time = 0

    def __init__(self, floor, weight, time):
        self.floor = floor
        self.weight = weight
        self.time = time

def ddirect(departure, arrival):
        destDir = 0
        if arrival.floor - departure.floor > 0:
            destDir = 1
        elif arrival.floor - departure.floor < 0:
            destDir = -1
        return destDir

class Elevator:
    passenger = 0
    dir = STOP
    door = CLOSE
    destUp = []
    destDown = []
    destAdd = []
    dest = []
    floor = 1
    time = 0

    def move(self, time):
        if self.door == CLOSE:
            if self.dir == STOP:
                self.time = time
            else:
                if (time - self.time) == MOVINGTIME:
                    if self.floor == self.dest[0].floor:
                        self.arrive(time)
                        self.door = OPEN

                    if self.dir == UP:
                        self.floor = self.floor + 1
                    elif self.dir == DOWN:
                        self.floor = self.floor - 1
                    self.time = time

        elif self.door == OPEN:
            if (time - self.time) == STOPTIME:
                self.time = time
                self.door = CLOSE

    def arrive(self, time):
        global passengerList
        self.passenger = self.passenger + self.dest[0].weight
        tempDest = self.dest.pop(0)

        if self.dir == UP:
            self.destUp.pop(0)
        elif self.dir == DOWN:
            self.destDown.pop(0)

        index = passengerSearch(passengerList, tempDest.time)
        passengerList[index].setArrivalTime(time)

        self.directionControl()

    def directionControl(self):
        if self.destAdd == []:
            if self.destUp == [] and self.destDown == []:
                self.dir = STOP
            elif self.destUp == [] and self.destDown != []:
                self.dir = DOWN
            elif self.destUp != [] and self.destDown == []:
                self.dir = UP
        else:
            if self.destUp != [] and self.destDown == []:
                self.dir = UP
                self.destUp = self.destAdd
                self.destAdd = []
            elif self.destUp == [] and self.destDown != []:
                self.dir == DOWN
                self.destDown = self.destAdd
                self.destAdd = []

    def destControl(self):
        if self.dir == STOP:
            if self.destUp != [] and self.destDown == []:
                self.dir = UP
            elif self.destUp == [] and self.destDown != []:
                self.dir = DOWN

        if self.dir == UP:
            self.dest = self.destUp + self.destDown + self.destAdd
        elif self.dir == DOWN:
            self.dest = self.destDown + self.destUp + self.destAdd




    def addDest(self, departure, arrival):

        destDir = ddirect(departure, arrival)
        destList = [departure, arrival]

        if self.dir == UP:
            if destDir == UP:
                if self.floor < departure.floor:
                    self.destUp = self.destUp + destList
                elif self.floor >= departure.floor:
                    self.destAdd = self.destAdd + destList
            elif destDir == DOWN:
                self.destDown = self.destDown + destList
        elif self.dir == DOWN:
            if destDir == UP:
                self.destUp = self.destUp + destList
            elif destDir == DOWN:
                if self.floor > departure.floor:
                    self.destDown = self.destDown + destList
                elif self.floor <= departure.floor:
                    self.destAdd = self.destAdd + destList
        elif self.dir == STOP:
            if destDir == UP:
                if self.floor <= departure.floor:
                    self.destUp = self.destUp + destList
                elif self.floor > departure.floor:
                    self.destDown = [departure]
                    self.destUp = [arrival]
                    self.dir = DOWN
            elif destDir == DOWN:
                if self.floor < departure.floor:
                    self.destUp = [departure]
                    self.destDown = [arrival]
                    self.dir = UP
                elif self.floor >= departure.floor:
                    self.destDown = self.destDown + destList

        self.destSort()
        self.destControl()
        self.directionControl()

        # print("destUplen : %d" % len(self.destUp))
        # print("destlen : %d" %len(self.dest))



    def destSort(self):
        if len(self.destUp) > 1:
            for i in range(len(self.destUp)):
                currentValue = self.destUp[i]
                position = i

                while position > 0 and self.destUp[position - 1].floor > currentValue.floor:
                    self.destUp[position] = self.destUp[position - 1]
                    position = position - 1
            self.destUp[position] = currentValue

        if len(self.destDown) > 1:
            for i in range(len(self.destDown)):
                currentValue = self.destDown[i]
                position = i

                while position > 0 and self.destDown[position - 1].floor < currentValue.floor:
                    self.destDown[position] = self.destDown[position - 1]
                    position = position - 1
            self.destDown[position] = currentValue

        if len(self.destAdd) > 1:
            if self.dir == UP:
                for i in range(len(self.destAdd)):
                    currentValue = self.destAdd[i]
                    position = i

                    while position > 0 and self.destAdd[position - 1].floor > currentValue.floor:
                        self.destAdd[position] = self.destAdd[position - 1]
                        position = position - 1
                self.destAdd[position] = currentValue
            elif self.dir == DOWN:
                for i in range(len(self.destAdd)):
                    currentValue = self.destAdd[i]
                    position = i

                    while position > 0 and self.destAdd[position - 1].floor < currentValue.floor:
                        self.destAdd[position] = self.destAdd[position - 1]
                        position = position - 1
                self.destAdd[position] = currentValue

    def totalTime(self):
        time = 0
        fromf = self.floor
        print("debug: self.dest len : %d " % len(self.dest))
        tof = self.dest[0].floor
        weight = self.passenger

        # for i in range(len(self.dest)-1):
        #     time = time + abs(self.dest[i+1].floor - self.dest[i].floor) * MOVINGTIME
        # time = time + len(self.dest) * STOPTIME

        for i in range(len(self.dest)-1):
            # print("fromf\ttof\tweight")
            # print("%d\t%d\t%d" % (fromf, tof, weight))
            time = time + abs(tof-fromf)*MOVINGTIME
            time = time + STOPTIME
            fromf = self.dest[i].floor
            tof = self.dest[i+1].floor
            weight = weight + self.dest[i].weight
            if weight > MAXLOAD:
                time = time * 10000

        print("totaltime : %d" % time)
        # for i in range(len(self.dest)):
        #     weight = weight + self.dest[i].weight
        #     if weight > MAXLOAD:
        #         time = time * 10000
        #         break

        return time


def evCall(ev1, ev2, ev3, passenger):
    # print("evcall!")
    #Destination(floor, weight, time)
    #Passenger: time, weight, departure, arrival
    departure = Destination(passenger.departure, passenger.weight, passenger.time)
    arrival = Destination(passenger.arrival, -passenger.weight, passenger.time)

    tempEv1 = copy.deepcopy(ev1)
    tempEv2 = copy.deepcopy(ev2)
    tempEv3 = copy.deepcopy(ev3)

    tempEv1.addDest(departure, arrival)
    tempEv2.addDest(departure, arrival)
    tempEv3.addDest(departure, arrival)
    # print("tempEV destlen : %d %d %d" %(tempEv1.dest))

    timeEv1 = tempEv1.totalTime()
    timeEv2 = tempEv2.totalTime()
    timeEv3 = tempEv3.totalTime()

    timeList = [timeEv1, timeEv2, timeEv3]

    selectedEv = timeList.index(min(timeList)) + 1

    if selectedEv == 1:
        # print("ev1 add")
        ev1.addDest(departure, arrival)
    elif selectedEv == 2:
        # print("ev2 add")
        ev2.addDest(departure, arrival)
    elif selectedEv == 3:
        # print("ev3 add")
        ev3.addDest(departure, arrival)

def passengerSearch(passengerList, time):
    for i in range(len(passengerList)):
        if passengerList[i].time == time:
            return i

    return -1



if __name__ == '__main__':
    global passengerList

    #timelist를 유저수만큼 랜덤하게 생성
    timelist = [1]
    time_num = random.randint(1, 30)
    for i in range(9):
        while time_num in timelist:
            time_num = random.randint(1, 30)
        timelist.append(time_num)
    timelist.sort()
    #passenger(time, weight, departure, arrival)
    passengerList = []
    for i in range(1, 11):
        p = Passenger(timelist[i-1], random.randint(1, 3), random.randint(1, 12), random.randint(1, 12))
        passengerList.append(p)

    for i in range(len(passengerList)):
        print("%d\t%d\t%d\t%d" %(passengerList[i].time, passengerList[i].weight, passengerList[i].departure, passengerList[i].arrival))

    #f1 = open("./RealTime.dat", 'w')
    #data = "time\tEv1.floor\tEv1.dir\t\tEv1.passenger\tEv2.floor\tEv2.dir\t\tEv2.passenger\tEv3.floor\tEv3.dir\t\tEv3.passenger\n"
    #f1.write(data)


    ev1 = Elevator()
    ev2 = Elevator()
    ev3 = Elevator()

    t = 0

    while t <= TMAX:
        print("t : %d" %t)

        #data = "%d\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n" % (t, ev1.floor, ev1.dir, ev1.passenger, ev2.floor, ev2.dir, ev2.passenger, ev3.floor, ev3.dir, ev3.passenger)
        #f1.write(data)

        passengerIndex = passengerSearch(passengerList, t)
        passenger = passengerList[passengerIndex]

        if passengerIndex != -1:
            evCall(ev1, ev2, ev3, passenger)

        ev1.move(t)
        ev2.move(t)
        ev3.move(t)

        print("ev1.floor : %d" % ev1.floor)
        print("ev1.passenger : %d" % ev1.passenger)
        print("ev1.dest")
        for i in range(len(ev1.dest)):
            print([ev1.dest[i].floor, ev1.dest[i].weight])
        print("ev1.dir : %d" % ev1.dir)
        #
        print(" ")
        #
        print("ev2.floor : %d" % ev2.floor)
        print("ev2.passenger : %d" % ev2.passenger)
        print("ev2.dest")
        for i in range(len(ev2.dest)):
            print([ev2.dest[i].floor, ev2.dest[i].weight])
        print("ev2.dir : %d" % ev2.dir)
        #
        print(" ")
        #
        print("ev3.floor : %d" % ev3.floor)
        print("ev3.passenger : %d" % ev3.passenger)
        print("ev3.dest")
        for i in range(len(ev3.dest)):
            print([ev3.dest[i].floor, ev3.dest[i].weight])
        print("ev3.dir : %d" % ev3.dir)

        print(" ")


        t = t + 1
        print(" ")

    #f2 = open("./passengerList.dat", 'w')
    #data = "time\tarrivalTime\tweight\t\tdeparture\tarrival\n"
    #f2.write(data)
    #for i in range(len(passengerList)):
    #    data = "%d\t%d\t\t%d\t\t%d\t\t%d\n" % (passengerList[i].time, passengerList[i].arrivalTime, passengerList[i].weight, passengerList[i].departure, passengerList[i].arrival)
    #    f2.write(data)

    #f1.close()
    #f2.close()
