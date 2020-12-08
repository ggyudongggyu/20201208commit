import sys
n , m = map(int, sys.stdin.readline().split())
s = [list(sys.stdin.readline()) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
Queue = [[0,0]]
s[0][0] = 1

while Queue:
    a = Queue[0][0]
    b = Queue[0][1]
    del Queue[0]
    for i in range(4):
        x = b + dx[i]
        y = a + dy[i]
        if 0<=x<m and 0<=y<n and s[y][x] == "1" :
            Queue.append([y, x])
            s[y][x] = s[a][b] + 1
print(s[n-1][m-1])

    
