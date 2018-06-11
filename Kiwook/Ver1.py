UP = 1
STOP = 0
DOWN = -1
MOVINGTIME = 5
STOPTIME = 10
MAXLOAD = 20
MAXFLOOR = 12
OPEN = 1
CLOSE = 0

class Elevator:
    weight = 0
    dir = STOP
    door = CLOSE
    destUp = []
    destDown = []
    destAdd = []
    dest = []
    floor = 1
    T = 0

    def arrive(self, time):
        self.weight += dest[0][1]
        a = dest.pop(0)
        if self.dir == UP:
            destUp.pop(0)
        elif self.dir == DOWN:
            destDown.pop(0)

        for i in range(len(passenger)):
            if passenger[i][0] == a[2]:
                passenger.append(time)

        #direction control
        if dest == []:
            self.dir == STOP
        if self.dir == UP * (dest[0][0] - a[0]) < 0:
            self.dir *= -1

    def totalTime(self, key):
        #key is the floor getting on used to calc overweight
        #returns integer
        time = 0
        w = self.weight

        if self.dir == UP:
            time = (2*self.destUp[-1][0] - 2*self.destDown[-1][0] + self.destAdd[-1][0] - self.floor) * MOVINGTIME + len(self.dest) * STOPTIME
        elif self.dir == DOWN:
            time = (2*self.destUp[-1][0] - 2*self.destDown[-1][0] - self.destAdd[-1][0] + self.floor) * MOVINGTIME + len(self.dest) * STOPTIME
        elif self.dir == STOP:
            time = abs(self.floor - dest[0][0]) * MOVINGTIME

        for i in range(len(dest)):  #weight cut
            w += dest[i][1]
            if w > MAXLOAD:
                time = time * 10000
                break

        return time

    def addDest(self, onlist, offlist):
        listToAdd = [onList, offList]
        if (offlist[0]-onList[0])/abs(offlist[0]-onList[0]) == UP:
            if self.dir == DOWN:
                destDown = destDown + listToAdd
                destDown.sort()
                destDown.reverse()
                dest = destDown + destUp + destAdd
            elif self.dir == UP:
                if onList[0] >= self.floor:
                    destUp = destUp + listToAdd
                    destUp.sort()
                    dest = destUp + destDown + offList
                elif onList[0] < self.floor:
                    destAdd = destAdd + listToAdd
                    destAdd.sort()
                    dest = destUp + destDown + destAdd
            elif self.dir == STOP:
                if onList[0] - self.floor >= 0:
                    destUp = destUp + listToAdd
                    destUp.sort()
                    dest = destUp + destDown + destAdd
                elif onList[0] - self.floor < 0:
                    destDown.append(onList)
                    destUp.append(offList)
                    dest.append(destDown)
                    dest.append(destUp)
        elif (offlist[0]-onList[0])/abs(offlist[0]-onList[0]) == DOWN:
            if self.dir == UP:
                destUp = destUp + listToAdd
                destUp.sort()
                dest = destUp + destDown + destAdd
            elif self.dir == DOWN:
                if onList[0] - self.floor <= 0:
                    destDown = destDown + listToAdd
                    destDown.sort()
                    destDown.reverse()
                    dest = destDown + destUp + destAdd
                elif onList[0] - self.floor > 0:
                    destAdd = destAdd + listToAdd
                    destAdd.sort()
                    destAdd.reverse()
                    dest = destUp + destDown + destAdd
            elif self.dir == STOP:
                if onList[0] - self.floor <= 0:
                    destDown = destDown + listToAdd
                    destDown.sort()
                    destDown.reverse()
                    dest = destDown + destUp + destAdd
                elif onList[0] - self.floor > 0:
                    destUp.append(onList)
                    destDown.append(offList)
                    dest.append(destUp)
                    dest.append(destDown)

    def move(self, time):
        if self.door == CLOSE:
            if self.dir == STOP:
                self.T = time
            elif self.dir == UP:
                if (time - self.T) == MOVINGTIME:
                    self.floor++
                    self.T = time
                    if floor == dest[0][0]:
                        self.arrive(time)
            elif self.dir == DOWN:
                if (time - self.T) == MOVINGTIME:
                    self.floor--
                    self.T = time
                    if floor == dest[0][0]:
                        self.arrive(time)
        elif self.door == OPEN:
            if (time - self.T) == STOPTIME:
                self.T = time
                self.door = CLOSE

def evCall(ev1, ev2, ev3, passengerListElement):
    on = [passengerListElement[2], passengerListElement[4], passengerListElement[0], passengerListElement[1]]
    off = [passengerListElement[3], passengerListElement[4], passengerListElement[0], passengerListElement[1]]

    tempEv1 = copy.deepcopy(ev1)
    tempEv2 = copy.deepcopy(ev2)
    tempEv3 = copy.deepcopy(ev3)

    tempEv1.addDest(on, off)
    tempEv2.addDest(on, off)
    tempEv3.addDest(on, off)

    timeEv1 = tempEv1.totalTime(on[0])
    timeEv2 = tempEv2.totalTime(on[0])
    timeEv3 = tempEv3.totalTime(on[0])

    timeList = [timeEv1, timeEv2, timeEv3]

    selectedEv = timeList.index(min(timeList)) + 1

    if selectedEv == 1:
        ev1.addDest()
    elif selectedEv == 2:
        ev2.addDest()
    elif selectedEv == 3:
        ev3.addDest()

def Search(list, key):
    for i in range(len(list)):
        if list[i][1] == key:
            return i

    return -1

if __name__ == '__main__':
    ev1 = Elevator()
    ev2 = Elevator()
    ev3 = Elevator()

    global passengerList = MakePassengerList()
    # passenger = [0id, 1time, 2departure, 3arrival, 4weight,] 5arrivalTime]
    # dest = [0floor, 1weight, 2id, 3time]
    t = 0

    while True:

        a = Search(passengerList, t) #return index
        if a != -1:
            #passengerList[a]에 대하여 call
            call(ev1, ev2, ev3, passengerList[a])

        ev1.move()
        ev2.move()
        ev3.move()
        t++

        if t == 10000:
            break
