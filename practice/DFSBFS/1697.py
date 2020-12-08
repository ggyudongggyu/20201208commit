import sys
from collections import deque

def sullae(matrix, N, K):
    q = deque()
    q.append(N)
    while q:
        i = q.popleft()
        if i == K :
            return matrix[i]
        for j in (i-1, i+1, i*2):
            if 0<=j<100001 and matrix[j] == 0:
                matrix[j] = matrix[i] + 1
                q.append(j)

N, K = map(int, sys.stdin.readline().split())
A = [0] * 100001
if N>=K:
    print(N-K)
else:
    print(sullae(A, N, K))