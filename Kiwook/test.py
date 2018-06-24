class Destination:
    floor = 0
    weight = 0
    time = 0

    def __init__(self, floor, weight, time):
        self.floor = floor
        self.weight = weight
        self.time = time

    def __repr__(self):
        return 'Destination(floor="%s", weight="%s", time="%s")' % (self.floor, self.weight, self.time)
    def keyfunc1(c):
        return c.floor
    def keyfunc2(c):
        return c.weight
    def keyfunc3(c):
        return c.time

if __name__ == '__main__':

    destList = [Destination(6, 2, 3), Destination(2, 3, 4), Destination(2, 5, 4), Destination(3, 4, 5), Destination(1, 2, 3)]

    destList.sort(key=Destination.keyfunc1)
    print(destList)

    print(destList[0].floor)
