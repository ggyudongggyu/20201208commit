#time = int(input()) -> input은 시간초과
import sys
time = int(sys.stdin.readline())
# 두개이상 값 받을 때는 map(int, sys.stdin.readline().split())
c=[]
for x in range(0,time):
    a,b=map(int, sys.stdin.readline().split())
    c.append(a+b)
for i in range(0,time):
    print(c[i])
