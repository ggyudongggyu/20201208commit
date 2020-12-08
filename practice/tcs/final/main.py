import shutil
member_cnt = int(input())
member_name = []
for i in range(member_cnt):
    member_name.append(str(input()))

# print(member_name)

for x in member_name:
    shutil.copy('sample.xlxs', '%s.xlxs' %(x))
    print('今回チームメンバーの名前は：%s' %(x))

 # wsl : windows store  - ubuntu - windows serve sysetems for linux [search]

# G folder > old_file.pdf
# shutil.copy('old_file.pdf' , 'new_file_name.pdf')


# ------------------------------------

from copy import CP
from namechange import CH

member_cnt = int(input())
name_lists = []
for i in range(member_cnt):
    name_lists.append(str(input()))

copyobj.copy()
