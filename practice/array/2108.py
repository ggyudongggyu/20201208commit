import sys
import math
from statistics import mean
from collections import Counter

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common() #1

    if len(nums) > 1 :
        if modes[0][1] == modes[1][1]: #2
            mod = modes[1][0]
        else :
            mod = modes[0][0]
    else :
        mod = modes[0][0] #3

    return mod

N = int(input())
dic = {}
for i in range(N):
    a = int(sys.stdin.readline())
    if a in dic:
        dic[a] =  dic[a] +1
    else:
        dic[a] = 1

sorted_dict = sorted(dic.items())
sorted_list = []

for i in range(len(sorted_dict)):
    for j in range(sorted_dict[i][1]):
        sorted_list.append(sorted_dict[i][0])

print(round(mean(sorted_list)))
print(sorted_list[math.trunc(N/2)])
print(mode(sorted_list))
print(abs(max(sorted_list)-min(sorted_list)))







# a=[]
#
# for i in range(time):
#     a.append(int(sys.stdin.readline()))
# a.sort()
# print(round(mean(a)))
# print(math.trunc(time/2))
#
# print(max(a)-min(a))
