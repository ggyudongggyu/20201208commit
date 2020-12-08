import sys
x = int(sys.stdin.readline())
if x==1:
    print(1,'/',1,sep='')
else:
    xx = x - 1
    cnt = 1
    y = 1
    while cnt+1<xx:
        cnt+=1
        xx-=cnt
        y += cnt
    d = cnt+1
    if d%2==0:
        print(x-y,'/',cnt+2-(x-y),sep='')
    else:
        print(cnt+2-(x-y),'/',x-y,sep='')
