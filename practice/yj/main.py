from member import Member
from member_management import registerMember
from member_management import dropout


member1 = Member('ym', 20200101)
member2 = Member('hj', 20200202)
member3 = ('jj', 20200303)
registerMember(member1)
registerMember(member2)
registerMember(member3)
# print(Member.member_list)

dropout('ym', 20200101)
dropout('yj', 20000702)
for x in Member.member_list:
    print("name:%s, birth_date:%d" % (x.getName(), x.getBirthDate()))
