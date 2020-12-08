from Student import Student
from Bag import Bag
yj = Student()
nikebag = Bag()
dg = Student()
adidas = Bag()
yj.bag = nikebag
dg.bag = adidas
yj.putItem(1, "laptop")
dg.putItem(1, "mouse")
nikebag.showItem(1)
adidas.showItem(1)
