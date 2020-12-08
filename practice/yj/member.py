class Member:
    member_list=[]
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
    def getName(self):
        return self.name
    def getBirthDate(self):
        return self.birth_date
