import sys
n, k = map(int, sys.stdin.readline().split())
s = []
dp = [0] * (k+1)
dp[0]=1
for i in range(n):
    s.append(int(input()))
for i in s:
    for j in range(1, k+1):
        if j >= i:
            dp[j] += dp[j-i]
print(dp[k])