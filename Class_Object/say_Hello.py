class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_Hello(self, to_name):
        print("안녕, " + to_name + "! 나는 " + self.name + "고, " + str(self.age)+"살이야.")

gyu = Person("동규", 24)
michael = Person("마이클", 22)
jenny = Person("제니", 30)

gyu.say_Hello("제니")
michael.say_Hello("마이클")
jenny.say_Hello("동규")
