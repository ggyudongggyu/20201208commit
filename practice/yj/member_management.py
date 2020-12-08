from member import Member

def registerMember(member):
    if type(member) == Member:
        Member.member_list.append(member)
        print("등록절차 완료")
    else:
        print("등록실패")

def dropout(name, birth_date):
    for x in Member.member_list:
        if name == x.getName() and birth_date==x.getBirthDate() :
            Member.member_list.remove(x)
            print("탈퇴 성공")
            return
    print("멤버가 아닙니다.")
