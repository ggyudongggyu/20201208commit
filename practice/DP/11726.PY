# x = int(input())
# dp = [0,1,2,3]
# if x <= 3:
#     print(dp[x]%10007)
# else:
#     for i in range(4, x+1):
#         dp.append(dp[i-1]+dp[i-2])
#     print(dp[x]%10007)

dp=[1,2]
x=int(input())
for i in range(2,x):
    dp.append(dp[i-1]+dp[i-2])
print(dp[x-1]%10007)