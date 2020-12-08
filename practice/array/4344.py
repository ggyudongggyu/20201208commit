import sys
import math
time=int(input())
aver_list=[]
rate=[]
for j in range(time):
    cnt=0
    score = list(map(int, sys.stdin.readline().split()))
    aver = (sum(score)-score[0])/score[0]
    aver_list.append(aver)
    for i in range(1, len(score)): # 왜 len(score)-1 이 아니지
        if score[i]>aver_list[j]:
            cnt = cnt+1
    rt = str(('%.3f' % round(100*cnt / (len(score)-1), 3)))+"%"
    rate.append(rt)
print(*rate)
