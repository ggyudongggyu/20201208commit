import sys
case = int(sys.stdin.readline())
c=[]
d=[]
for x in range(0,case):
    a,b = map(int, sys.stdin.readline().split())
    c.append(a+b)
    d.append(str(a)+" + "+str(b))
for i in range(0,case):
    print("Case #"+str(i+1)+": "+str(d[i])+" = "+str(c[i]))
