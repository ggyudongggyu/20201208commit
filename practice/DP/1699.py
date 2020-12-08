# import math
# x = int(input())
# dp = [0, 1, 2, 3]
# z = 1
# for i in range(4, x+1):
#     if z != math.trunc(i**0.5):
#         z = math.trunc(i**0.5)
#         dp.append(1)
#     else:
#         dp.append(min(dp[z**2] + dp[i-z**2], dp[(z-1)**2]+dp[i-(z-1)**2]))
#         # dp.append(min(dp[z**2] + dp[i-z**2], dp[(z-1)**2]+dp[i-(z-1)**2]))

# print(dp[x])

x = int(input()) 
dp = [0] * (x+1) 
for i in range(1, x+1): 
    dp[i] = i 
    for j in range(1, i): 
        if (j * j) > i: 
            break 
        dp[i] = min(dp[i], dp[i - j**2] + 1) 

print(dp[x])

