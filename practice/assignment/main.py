from Father import Father
from Son import Son
father1 = Father(10000000)
son1 = Son(0, father1)
father1.son = son1
father1.giveMoney(30000)
father1.showMoney()
son1.showMoney()
