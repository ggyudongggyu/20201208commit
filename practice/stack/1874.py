case = int(input())
case_list = []
print_list = []
cnt = 1
temp = True
for _ in range(case):
    x = int(input())
    while cnt <= x :
        case_list.append(cnt)
        print_list.append('+')
        cnt += 1
    if case_list[-1]==x:
        case_list.pop()
        print_list.append('-')
    else:
        temp= False
if temp==False:
    print('NO')
else:
    for i in print_list:
        print(i)
    