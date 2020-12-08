# time=int(input())
# aver_list=[]
# for _ in range(time):
#     num = int(input())
#     for i in range(num):
#         score=map(int, input().split())
#         score_sum+=score
#     score_aver=score_sum/num
#     aver_list.append(score_ever)
# print(*aver_list)
import sys
time=int(input())
aver_list=[]
for _ in range(time):
    score = list(map(int, sys.stdin.readline().split()))
    aver = (sum(score)-score[0])/score[0]
    aver_list.append(aver)
print(*aver_list)
