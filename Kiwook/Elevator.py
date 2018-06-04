# constant
UP = 1
STOP = 0
DONW = -1
MOVINGTIME = 5
STOPTIME = 10
MAXLOAD = 20
MAXFLOOR = 12

class Elevator:
    passenger = 0
    dir = STOP
    destUp = []
    destDown = []
    destAdd = []
    dest = []
    floor = 1

    def getOn(self): #무게 추가

    def getOff(self): #무게 감소 및 목적지 리스트 요소 삭제

    def addDest(self, onList, offList):
        listToAdd = [onList, offList]
        if (offlist[0]-onList[0])/abs(offlist[0]-onList[0]) == UP:
            if self.dir == DOWN:
                destDown = destDown + listToAdd
                destDown.sort()
                destDown.reverse()
                dest = destDown + destUp + destAdd
            elif self.dir == UP:
                if onList[0] - self.floor >= 0:
                    destUp = destUp + listToAdd
                    destUp.sort()
                    dest = destUp + destDown + offList
                elif onList[0] - self.floor < 0:
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
        #if dest = [] dir = stop
        # if dest[0][0] > dest[0][1] dir = DOWN

    def totalTime: #엘리베이터 승객들의 전체 예상 소요시간을 계산



def call(ev1, ev2, ev3, passenger, startingPoint, destination, to):
    onList = [startingPoint, passenger]
    offList = [destination, -passenger]

    tempEv1 = ev1
    tempEv2 = ev2
    tempEv3 = ev3

    # weight cut


    #tempEv에 각각 넣어서 토탈 타임을 계산해보고 가장 적은 엘리베이터에 배차
    if tempEv1.totalTime() <= tempEv2.totalTime() and tempEv1.totalTime() <= tempev3.totalTime():
        ev1.addDest(onList, offList)
    elif tempEv2.totalTime() <= tempEv1.totalTime() and tempEv1.totalTime() <= tempev1.totalTime():
        ev2.addDest(onList, offList)
    elif tempEv3.totalTime() <= tempEv1.totalTime() and tempEv3.totalTime() <= tempev2.totalTime():
        ev3.addDest(onList, offList)
