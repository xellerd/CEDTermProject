import copy

UP = 1
STOP = 0
DOWN = -1
MOVINGTIME = 2
STOPTIME = 5
MAXLOAD = 20
MAXFLOOR = 12
OPEN = 1
CLOSE = 0

TMAX = 50

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

    #엘리베이터가 목적지에 도착했을 떄
    def arrive(self, time):
        print("arrived")
        global passengerList
        self.weight += self.dest[0][1]   # 무게 컨트롤
        a = self.dest.pop(0)             # 목적지 목록에서 삭제

        if self.dir == UP:
            self.destUp.pop(0)
        elif self.dir == DOWN:
            self.destDown.pop(0)

        for i in range(len(passengerList)):
            print("passengerList[%d][0] : %d a[2] : %d" % (i, passengerList[i][0], a[2]))
            if passengerList[i][0] == a[2]:
                passengerList[i].append(time)   #도착시간을 passengerList에 추가, 탄 시간에서 빼면 소요시간 나옴
                print(passengerList)

        #direction control
        if self.dest == []:
            self.dir = STOP
        elif self.dir == UP * (self.dest[0][0] - a[0]) < 0:
            self.dir = self.dir * (-1)

    # 총 소요 시간 계산용 함수인데 디버깅 필요
    def totalTime(self, key):
        #key is the floor getting on used to calc overweight
        #returns integer
        time = 0
        w = self.weight
        # dest = [0floor, 1weight, 2id, 3time]

        for i in range(len(self.dest)-1):
            time = time - self.dest[i][0] + self.dest[i+1][0]
        time = abs(time)
        time = time * MOVINGTIME
        time = time + len(self.dest) * STOPTIME
        time = abs(time)

        # if self.dir == UP:
        #     for i in range(len(dest)-1):
        #         time = time - dest[i][0] + dest[i+1][0]
        #     time = abs(time)
        #     time = time * MOVINGTIME
        #     time = time + len(self.dest) * STOPTIME
        #     time = abs(time)
        # elif self.dir == DOWN:
        #     time = (2*self.destUp[-1][0] - 2*self.destDown[-1][0] - self.destAdd[-1][0] + self.floor) * MOVINGTIME + len(self.dest) * STOPTIME
        # elif self.dir == STOP:
        #     time = abs(self.floor - self.dest[0][0]) * MOVINGTIME
        for i in range(len(self.dest)):  #weight cut
            w = w + self.dest[i][1]
            if w > MAXLOAD:
                time = time * 10000
                break

        return time

    #엘리베이터가 나와 어떤 위치에서 어떤 방향으로 이동중인지 경우의 수 만큼 생성...
    def addDest(self, on, off):
        listToAdd = [on, off]
        if (off[0]-on[0])/abs(off[0]-on[0]) == UP:
            if self.dir == DOWN:
                self.destDown = self.destDown + listToAdd
                self.destDown.sort()
                self.destDown.reverse()
                self.dest = self.destDown + self.destUp + self.destAdd
            elif self.dir == UP:
                if on[0] >= self.floor:
                    self.destUp = self.destUp + listToAdd
                    self.destUp.sort()
                    self.dest = self.destUp + self.destDown + self.destAdd
                elif on[0] < self.floor:
                    self.destAdd = self.destAdd + listToAdd
                    self.destAdd.sort()
                    self.dest = self.destUp + self.destDown + self.destAdd
            elif self.dir == STOP:
                if on[0] - self.floor >= 0:
                    self.destUp = self.destUp + listToAdd
                    self.destUp.sort()
                    self.dest = self.destUp + self.destDown + self.destAdd
                    self.dir = UP
                elif on[0] - self.floor < 0:
                    self.destDown.append(on)
                    self.destUp.append(off)
                    self.dest = self.dest + self.destDown
                    self.dest = self.dest + self.destUp
                    # self.dest.append(self.destDown)
                    # self.dest.append(self.destUp)
                    self.dir = DOWN
        elif (off[0]-on[0])/abs(off[0]-on[0]) == DOWN:
            if self.dir == UP:
                self.destUp = self.destUp + listToAdd
                self.destUp.sort()
                self.dest = self.destUp + self.destDown + self.destAdd
            elif self.dir == DOWN:
                if on[0] - self.floor <= 0:
                    self.destDown = self.destDown + listToAdd
                    self.destDown.sort()
                    self.destDown.reverse()
                    self.dest = self.destDown + self.destUp + self.destAdd
                elif on[0] - self.floor > 0:
                    self.destAdd = self.destAdd + listToAdd
                    self.destAdd.sort()
                    self.destAdd.reverse()
                    self.dest = self.destUp + self.destDown + self.destAdd
            elif self.dir == STOP:
                if on[0] - self.floor <= 0:
                    self.destDown = self.destDown + listToAdd
                    self.destDown.sort()
                    self.destDown.reverse()
                    self.dest = self.destDown + self.destUp + self.destAdd
                    self.dir = DOWN
                elif on[0] - self.floor > 0:
                    self.destUp.append(on)
                    self.destDown.append(off)
                    self.dest = self.dest + self.destUp
                    self.dest = self.dest + self.destDown
                    self.dir = UP
                    # self.dest.append(self.destUp)
                    # self.dest.append(self.destDown)

    def move(self, time):
        # OPEN은 목적지에 도착했을 시 MOVINGTIME만큼 기다리기 위한 장치
        if self.door == CLOSE:
            if self.dir == STOP:
                # 아무것도 안할 경우 시간 계속 갱신
                self.T = time
            elif self.dir == UP:
                # MOVINGTIME만큼 시간이 흐르면 floor ++, 시간 갱신, floor가 다음 목적지와 같으면 arrive함수 실행
                # (이전에는 T 갱신을 안하기 때문에 while문이 돌 동안 T-time이 MOVINGTIME과 같아질때까지 증가)
                if (time - self.T) == MOVINGTIME:
                    self.floor = self.floor + 1
                    self.T = time
                    if self.floor == self.dest[0][0]:
                        self.arrive(time)
                        self.door = OPEN
            elif self.dir == DOWN:
                if (time - self.T) == MOVINGTIME:
                    self.floor = self.floor - 1
                    self.T = time
                    if floor == dest[0][0]:
                        self.arrive(time)
                        self.door = OPEN
        # 정지 시 STOPTIME만큼 대기
        elif self.door == OPEN:
            if (time - self.T) == STOPTIME:
                self.T = time
                self.door = CLOSE

def evCall(ev1, ev2, ev3, passengerListElement):
    # 데스티네이션에 넣기 좋게 정제
    on = [passengerListElement[2], passengerListElement[4], passengerListElement[0], passengerListElement[1]]
    off = [passengerListElement[3], -passengerListElement[4], passengerListElement[0], passengerListElement[1]]

    # 시간 비교를 위한 임시 인스턴스
    tempEv1 = copy.deepcopy(ev1)
    tempEv2 = copy.deepcopy(ev2)
    tempEv3 = copy.deepcopy(ev3)

    # 임시 인스턴스에 각각 같은 목적지 추가
    tempEv1.addDest(on, off)
    tempEv2.addDest(on, off)
    tempEv3.addDest(on, off)

    # 토탈 타임 계산
    timeEv1 = tempEv1.totalTime(on[0])
    timeEv2 = tempEv2.totalTime(on[0])
    timeEv3 = tempEv3.totalTime(on[0])

    timeList = [timeEv1, timeEv2, timeEv3]

    # 토탈타임이 미니멈인 엘리베이터를 찾아서 실제로 목적지 추가
    selectedEv = timeList.index(min(timeList)) + 1

    if selectedEv == 1:
        ev1.addDest(on, off)
        print("call ev1")
    elif selectedEv == 2:
        ev2.addDest(on, off)
        # print("call ev2")
    elif selectedEv == 3:
        ev3.addDest(on, off)
        # print("call ev3")

# 일반적인 순차검색
def Search(list, key):
    for i in range(len(list)):
        if list[i][1] == key:
            return i

    return -1

if __name__ == '__main__':
    global passengerList #사람이 내렸을 때 시간요소를 추가하기 위해 전역변수 설정

    #엘리베이터 인스턴스 생성
    ev1 = Elevator()
    ev2 = Elevator()
    ev3 = Elevator()

    # 임의의 패신저리스트
    passengerList = [[0, 2, 4, 6, 7], [1, 5, 7, 3, 3], [2, 18, 8, 9, 3]]

    # 가독성이 안좋긴 한데 일단 임시로 패신저랑 데스티네이션 엘리먼트 설명입니다. 패신저는 5개 요소로 작성하고 마지막에 append이용해서 arrivalTime 추가
    # passenger = [0id, 1time, 2departure, 3arrival, 4weight,] 5arrivalTime]
    # dest = [0floor, 1weight, 2id, 3time]

    t = 0

    while t <= TMAX:
        # 디버깅용
        print(t)

        # 패신저리스트의 시간과 반복문의 시간 비교해서 인텍스 뽑아냄
        a = Search(passengerList, t) #return index
        # 검색 실패하면 -1 return
        if a != -1:
            #passengerList[a] 파라미터로 넘겨주면서 Elevator call
            evCall(ev1, ev2, ev3, passengerList[a])

        # move 한번씩 실행해주고 다른 메소드는 무브 안에서 호출

        ev1.move(t)
        ev2.move(t)
        ev3.move(t)

        print(ev1.dest)
        print("floor: %d" % ev1.floor)
        print("ev1.T : %d" % ev1.T)
        print("ev1.dir : %d" % ev1.dir)

        t = t + 1
        print()

    print("passengerList : ")
    print(passengerList)
