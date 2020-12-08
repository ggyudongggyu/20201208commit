class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_Hello(self, to_name):
        print("hello, " + to_name + "! i am  " + self.name + "and, " + str(self.age)+"age old.")

class Police(Person):
    def taihou(self, darewo):
        print("stop , "+darewo+"!")

class Student(Person):
    def bennkyou(self, kamoku):
        print("today is  "+ kamoku + " bennkyou siyo")

class tcs(Person):
    def itconsaru(self, consaru):
        print(consaru, "service wo simasyou")


gyu = Person("donggyu", 24)
shingo = Student("sonehara", 22)
shimizu = Police("shimizu", 30)
A = tcs("namae", 30)

shimizu.taihou("donggyu")
shingo.bennkyou("math, python")
A.itconsaru("python")
A.say_Hello("shingo")