# glasses = int(input())
# A = []
# p= []
# for i in range(glasses):
#     A.append(int(input()))
#     p.append([0,0,0])
# p[0][0] = p[0][2] = A[0]

# for i in range(1, glasses):
#     if i % 3 == 1:
#         p[i][0] = p[i-1][0] + A[i]
#         p[i][1] = p[i-1][1] + A[i]
#         p[i][2] = p[i-1][2]
#     elif i % 3 == 2:
#         p[i][1] = p[i-1][1] + A[i]
#         p[i][2] = p[i-1][2] + A[i]
#         p[i][0] = p[i-1][0]
#     else:
#         p[i][0] = p[i-1][0] + A[i]
#         p[i][1] = p[i-1][1]
#         p[i][2] = p[i-1][2] + A[i]
# print(p)
# print(max(max(p[-1]), max(p[-2])))

# # 반례 1, 15, 2, 20, 3, 60
# # 케이스의 분류를너무 적고 멋대로 일반화시켜버림.

n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])
