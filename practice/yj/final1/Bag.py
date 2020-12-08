class Bag:
    def __init__(self):
        self.pocket1 = None
        self.pocket2 = None
        self.pocket3 = None
        self.pocket4 = None

    def showItem(self, pocket_number):
        if pocket_number == 1:
            print("1번째 가방:", self.pocket1)
        elif pocket_number == 2:
            print("2번째 가방:", self.pocket2)
        elif pocket_number == 3:
            print("3번째 가방:", self.pocket3)
        else:
            print("4번째 가방:", self.pocket4)
