import sys
K, N = map(int, sys.stdin.readline().split())
A = []
for _ in range(K):
    A.append(int(sys.stdin.readline()))
i = 1
f = max(A)
while(i <= f):
    m = (i+f)//2
    ans = 0 
    for j in range(K):
        ans += A[j]//m
    if ans >= N :
        i = m+1
    else:
        f = m-1
    # print(m)
print(f)