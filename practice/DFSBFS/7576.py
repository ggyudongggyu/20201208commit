import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
q = [list(map(int, input().split())) for _ in range(n)]
temp = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    for j in range(m):
        if q[i][j] == 1 :
            temp.append([i, j])
while temp:
    for a in range(len(temp)):
        y , x = temp.popleft()
        for b in range(4):
            ny = y + dy[b]
            nx = x + dx[b]
            if 0<=ny<n and 0<=nx<m and q[ny][nx] == 0:
                q[ny][nx] = q[y][x] + 1
                temp.append([ny, nx])
    # for z in range(len(q)):
    #     print(q[z], end='\n')
    # print("====================")

isTrue = False
result = -2
for i in q:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)  
