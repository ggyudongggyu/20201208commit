class Father:
    def __init__(self, money):
        self.money = money
        self.son = None

    def giveMoney(self, money):
        self.money = self.money - money
        self.son.getMoney(money)

    def showMoney(self):
        print(self.money)
