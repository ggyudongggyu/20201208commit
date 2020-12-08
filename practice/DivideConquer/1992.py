import sys
n=int(sys.stdin.readline()) 
mat=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def dnq(x, y, n):
    now = mat[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if now != mat[i][j]:
                print('(',end='')
                dnq(x, y, n//2)#1사분면
                dnq(x, y+n//2, n//2) #2사분면
                dnq(x+n//2, y, n//2) #3사분면
                dnq(x+n//2, y+n//2, n//2) #4사분면
                print(')',end='')
                return
    if now == 0:
        print(0, end='')
        return
    else:
        print(1, end='')
        return
dnq(0,0,n)