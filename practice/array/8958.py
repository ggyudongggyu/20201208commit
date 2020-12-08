times=int(input())
sum_list=[]
for _ in range(0,times):
    ox=str(input())
    ox_list=list(ox)
    sum=0
    count=1
    for i in range(len(ox_list)):
        if ox_list[i]=='O':
            sum+=count
            count+=1
        else:
            count=1
    sum_list.append(sum)
print(*sum_list)
