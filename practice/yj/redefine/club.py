class Club:
    def __init__(self, univ_name):
        self.univ_name = univ_name
        self.club_mem = []
    def __add__(self, mem):
        if mem.univ_name == self.univ_name :
            print("success")
            self.club_mem.append(mem)
        else:
            print("fail")

        #1. cau 판단
        #2-1 . 석세스,  #3 .페일 결과도 프린트해야함
        #2-2 . list에 요소 추가

    def showMemName(self):
        for mem in self.club_mem:
            print(mem.name)

class Member:
    def __init__(self, univ_name, name):
        self.univ_name = univ_name
        self.name = name

club = Club("cau")
mem1 = Member("cau", "ym")
mem2 = Member("cau", "yj")
mem3 = Member("ssu", "hj")
club + mem1
club + mem2
club + mem3
club.showMemName()
# print(club.club_mem)
