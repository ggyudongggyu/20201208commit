class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printinfo(self):
        print('name : ',self.name, 'age : ',self.age)
    def __add__(self, number):
        self.age = self.age + number
profile1 = Profile('ym', 50)
profile1.printinfo()
profile1+1 #profile1.__add__(1)
profile1.printinfo
