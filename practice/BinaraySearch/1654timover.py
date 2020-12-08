# 4 7  항상 K<=N
# 802 3     3   4
# 743  3    3   3
# 457  2    2   2
# 539 2     2   2
import sys
K, N = map(int, sys.stdin.readline().split())
A = []
ans = [0 for _ in range(K)]

for _ in range(K):
    A.append(int(sys.stdin.readline()))
mini = min(A)
ex_mini = mini
while (True):
    mini //= 2

    for i in range(K):
        ans[i] = A[i]//mini
    if sum(ans) >= N:
        break
    ex_mini = mini


avr = (mini+ex_mini)//2
for i in range(K):
    ans[i] = A[i]//avr
if sum(ans) >= N:
    while(sum(ans)>=N):
        avr += 1
        for i in range(K):
            ans[i] = A[i]//avr
    avr -= 1
else:
    while (sum(ans) < N):
        avr -= 1
        for i in range(K):
            ans[i] = A[i]//avr
print(avr)



# while (True):
#     for i in range(K):
#         ans[i] = A[i] // avr
#     if sum(ans) < N:
#         mini = avr
#     else : ex_mini = avr
# print(mini-1)