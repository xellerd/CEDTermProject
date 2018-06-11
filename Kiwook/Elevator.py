# constant
UP = 1
STOP = 0
DONW = -1
MOVINGTIME = 5
STOPTIME = 10
MAXLOAD = 20
MAXFLOOR = 12
OPEN = 1
CLOSE = 0

class Elevator:
    passenger = 0
    dir = STOP
    door = 0
    destUp = []
    destDown = []
    destAdd = []
    dest = []
    floor = 1

    # def getOn(self): #무게 추가
    #
    # def getOff(self): #무게 감소 및 목적지 리스트 요소 삭제
    passenger = [id, time, departure, arrival, arrivalTime]
    dest = [floor, weight, id, time]

    def getOnOff(self):
        self.passenger += dest[0][1]

    def addDest(self, onList, offList):
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


    def move: #엘리베이터 방향 제어, 목적지 리스트를 기반으로 엘리베이터의 움직임 제어
        if dir == STOP:
            T = t
        else:
            if self.door == CLOSE:
                if (t-T) == MOVINGTIME:
                    if self.dir == UP:
                        self.floor++
                    else if self.dir == DOWN:
                        self.floor--
                    T = t
                    if floor == dest[0][0]:
                        self.getOnOff()
                        del a[0]
                        self.door = OPEN
            else if self.door == OPEN:
                if (t-T) == STOPTIME:
                    T = t
                    self.door = CLOSE

    move 함수 on 1 off 2 move 3 stop = 0



    def totalTime: #엘리베이터 승객들의 전체 예상 소요시간을 계산



def call(ev1, ev2, ev3, passenger, startingPoint, destination, to):
    onList = [startingPoint, passenger]
    offList = [destination, -passenger]

    tempEv1 = ev1
    tempEv2 = ev2
    tempEv3 = ev3

    tempEv1.addDest(onList, offList)
    tempEv2.addDest(onList, offList)
    tempEv3.addDest(onList, offList)

    # weight cut
    expect1 = ev1.passenger
    for i in ev1.dest:
        if ev1.dest[i][0] <= startingPoint:
            expect1 += dest[i][1]
    #if expect1 > MAXLOAD->버림

<<<<<<< HEAD
    # tempEv 목적지 추가

=======
>>>>>>> d51da128fd213d3313dfba7e3bae4a67f6243c68
    #tempEv에 각각 넣어서 토탈 타임을 계산해보고 가장 적은 엘리베이터에 배차

    timeList = [tempEv1.totalTime(), tempEv2.totalTime(), tempev3.totalTime()]
    timeList.index(min(timeList))


#main
ev1 = Elevator()
ev2 = Elevator()
ev3 = Elevator()

randomList = [index, time, passenger, startingPoint, destination, time2]

t = 0
while True:
    ev1.move()
    ev2.move()
    ev3.move()

    #search randomList
    #if time == t:
        # call(ev1, ev2, ev3, randomListElement):



    t++
