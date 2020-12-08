class Son:
    def __init__(self, money, father):
        self.money = money
        self.father = father

    def givemeMoney(self, money):
        self.father.giveMoney(money)

    def getMoney(self, money):
        self.money = self.money + money

    def showMoney(self):
        print(self.money)
