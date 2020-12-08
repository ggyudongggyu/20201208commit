def dnq(x, y, k):
    global white, blue
    now_color = mat[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if now_color != mat[i][j] :
                dnq(x, y, k//2) #1사분면
                dnq(x, y+k//2, k//2) #2사분면
                dnq(x+k//2, y, k//2) #3사분면
                dnq(x+k//2, y+k//2, k//2) #4사분면
                return
    if now_color == 1: #all blue
        blue += 1
        return
    else: # all white 
        white += 1
        return
    
k=int(input())
mat = []
for i in range(k):
    mat.append(list(map(int, input().split())))

white = 0 #0이면 하얀색, 초기화
blue = 0 #1이면 파란색, 초기화
dnq(0,0,k)
print(white)
print(blue)