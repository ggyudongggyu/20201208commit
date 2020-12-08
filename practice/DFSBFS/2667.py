import sys
n = int(sys.stdin.readline())
mat = [list(sys.stdin.readline()) for _ in range(n)]
cnt = 0
result = [] #결과값 저장할 리스트
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1] #이동기

def apt(y , x): #함수 자체가 1이면 실행되는 함수
    global cnt
    mat[y][x] = '0'       # 1이면 0으로 바꿔주고 (애초에 숫자형 리스트로 받은게 아니라 싹다 문자로 되어있음 . 확인하고 싶으면 mat 출력해보기.)
    cnt += 1                #cnt 하나 늘려줌
    for k in range(4):      #4의 의미는 상하좌우
        now_y = y + dy[k]
        now_x = x + dx[k]
        if 0 <= now_x < n and 0 <= now_y < n and mat[now_y][now_x]=='1':
            apt(now_y, now_x)

for y in range(n):
    for x in range(n):
        if mat[y][x] == '1':
            cnt = 0
            apt(y, x)
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i)
