import sys
size = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline()) for _ in range(size)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0 #몇 채인지 새는거
result = [] #몇 채인지 다 세고 여기에 추가해줄 것.

def apt(y, x):
    global cnt
    matrix[y][x] = '0'
    cnt += 1
    for a in range(4):
        next_y = y + dy[a]
        next_x = x + dx[a]
        if 0<=next_y<size and 0<=next_x<size and matrix[next_y][next_x] == '1' :
            apt(next_y, next_x)

for y in range(size):
    for x in range(size):
        if matrix[y][x] =='1':
            cnt = 0
            apt(y, x)
            result.append(cnt) #몇 채인지 셌던 걸 result에 추가해준 것.
print(len(result))
result.sort()
print(*result, sep='\n')
