x = int(input())
a = list(map(int, input().split()))
z = int(input())
queue = [z]
result_list = []
result_cnt = 0
if len(a)==1 or a[z]==-1:
    print(0)
else:
    a[z]=-1
    while queue:
        r = queue.pop(0)
        for i in range(len(a)):
            if a[i]==r:
                queue.append(i)
                a[i] = -1
    for i in range(len(a)):
        if a[i]!=-1:
            result_list.append(i)
    if not result_list:
        print(1)
    else:
        for i in result_list:
            if i in a:
                result_cnt += 1
        print(len(result_list)-result_cnt)