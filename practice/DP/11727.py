x = int(input())
dp=[1,3]
for i in range(2,x+1):
    dp.append(dp[i-1] + 2*dp[i-2])
print(dp[x-1]%10007)
