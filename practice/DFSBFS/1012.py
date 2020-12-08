import sys
sys.setrecursionlimit(100000)

test = int(sys.stdin.readline())
dY = [0,0,-1,1]
dH = [1,-1,0,0]
result=[]
    
def prevent(Y, H):
    matrix[H][Y] = 0
    for a in range(4):
        next_Y = Y + dY[a]
        next_H = H + dH[a]
        if 0<=next_Y<tY and 0<=next_H<tH and matrix[next_H][next_Y]==1:
            prevent(next_Y, next_H)

for _ in range(test):
    cnt = 0
    tY, tH, B = map(int, sys.stdin.readline().split())
    matrix = [[0] * (tY+1) for _ in range(tH+1)]
    for _ in range(B):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    
    for i in range(tH):
        for j in range(tY):
            if matrix[i][j] == 1:
                prevent(j, i)
                cnt += 1
    result.append(cnt)
print(*result, sep='\n')