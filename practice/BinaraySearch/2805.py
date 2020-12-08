# N그루  M미터
# 20 15 10 17
import sys
from sys import stdin
N , M = map(int, sys.stdin.readline().split())
A = list(map(int, stdin.readline().split()))
i, f = 1, max(A)

while (i <= f):
    cnt = 0
    m = (i+f)//2
    for j in A:
        if m < j:
            cnt += (j-m)
    if cnt >= M:
        i = m+1
    else : f = m-1
print(f)