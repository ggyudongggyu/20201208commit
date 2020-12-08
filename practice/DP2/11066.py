# n = int(input())
# s = list(map(int, input().split()))
# dp = [0] * (n+1)
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# for i in range(2, len(s)):
#     dp[i] = min(dp[i-2] + s[i-1], s[i-1]+s[i])


# print(dp)
# print(s)

# s=[40,30,30,50]
# print(sum(s[0:3]))
# print(sum(s[2:-1]))

import sys
input = sys.stdin.readline
t = int(input()) 
for __ in range(t):
    k = int(input()) 
    page = list(map(int, input().split())) 
    table = [[0]*k for _ in range(k) ]
    for i in range(k-1): 
        table[i][i+1] = page[i] + page[i+1] 
        for j in range(i+2, k): 
            table[i][j] = table[i][j-1] + page[j]
    print(table)
    for d in range(2, k): # diagonal
        for i in range(k-d):
            j = i+d
            minimum = [table[i][x] + table[x+1][j] for x in range(i, j)]
            print(minimum)
            table[i][j] += min(minimum)
    print(table[0][k-1])
    
    print(table)
