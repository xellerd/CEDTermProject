class P:
    element1 = 0
    element2 = 0
    element3 = 0

    def __init__(self, element1, element2, element3):
        self.element1 = element1
        self.element2 = element2
        self.element3 = element3

if __name__ == '__main__':
    p1 = P(1, 2, 3)
    list = [P(2, 3, 4)]
    print(list[0].element1, list[0].element2)