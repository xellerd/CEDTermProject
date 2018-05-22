class Elevator:
    def __init__(self, passenger, direction, destination1, destination2, elevatorFloor):
        self.passenger = passenger
        self.direction = direction
        self.destinationUp = destinationUp
        self.destinationDown = destinationDown
        self.elevatorFloor = elevatorFloor

    def call(self, floor, direction):
        #[0, floor]를 한 요소로 self.destinationUp or self.destinationDown에 append, sort, reverse if nesessary

    def take(self, number, destination):
        #[number, destination]을 한 요소로 self.destinationUp or self.destinationDown에 append, sort, reverse if nesessary
        #sum(number)를 passenger에 ++
    def getoff(self, floor):
        #floor == elevatorFloor면 destination list의 [number, floor]를 삭제하고 sum(x)를 passenger에서 --
    def move:
        #엘리베이터 이동 기술

    #시간에 따른 이동 표현 어떻게?


# 새 엘리베이터 배차 방법
# method 1:
#     1. 인원 초과가 예상될 경우 제외(경로상에서 추가, 제외 될 인원 예상해야 함)
#     2. 가장 빨리 올 수 있는 엘리베이터 배차(이동 층 * 이동 층 당 시간 + 정지 층 * 정지 당 시간)->minimum
#     3. 방향 고려 필요 없다(조건 2에 의해)
#
# method 2:
#     1. 모든 엘리베이터에 가상으로 추가를 함
#     2. 엘리베이터 탑승 인원의 소요시간을 모두 sum
#     3. sum이 minimum인 경우에 탑승
