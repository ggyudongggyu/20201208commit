import sys
from sys import stdin
N = int(sys.stdin.readline())
A = list(map(int, stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, stdin.readline().split()))

d = {}
for i in A:
    if i in d:
        d[i]+=1
    else: d[i]=1

for j in B:
    try:
        print(d[j], end=' ')
    except KeyError as e:
        print(0, end=' ')
