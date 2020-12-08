# N = int(input())
# A = list(map(int, input().split()))
# # mmax = A[0]
# # A.append(False)
# B = [0]*(N)
# for i in range(N):
#     for j in range(i, N):
#         if i==j:
#             B[j] = A[j]
#         else:
#             B[j] = B[j-1] + A[j]
#     B[i] = max(B)
    
#     # if max(B) > mmax : 
#     #     mmax = max(B)
# print(max(B))

import sys
n = int(sys.stdin.readline()) 
arr = list(map(int, sys.stdin.readline().split())) 
max_val = arr[0] 
tmax = arr[0] 
for t in arr[1:]: 
    if tmax < 0 and t > 0: tmax = t 
    else: tmax += t 
    max_val = max(max_val, tmax, t)

print(max_val)