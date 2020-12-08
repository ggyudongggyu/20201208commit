import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
s=[]
for i in range(m):
    s.append(list(map(int, list(input().strip()))))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    q = deque()
    q.append([0,0,1])
    his = [[[0] * 2 for _ in range(n)] for _ in range(m)]
    his[0][0][1] = 1
    while q:
        a, b, c = q.popleft()
        if a==m-1 and b==n-1 :
            return his[a][b][c]
        for i in range(4):
            nx = b + dx[i]
            ny = a + dy[i]
            if 0<=ny<m and 0<=nx<n:
                if s[ny][nx] == 1 and c==1:
                    his[ny][nx][0] = his[a][b][c] + 1
                    q.append([ny,nx,0])
                elif s[ny][nx] == 0 and c==0:
                    his[ny][nx][0] = his[a][b][c] + 1
                    q.append([ny,nx,c])
    return -1
print(bfs())
