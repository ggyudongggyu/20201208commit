import sys

time = int(input())
a=[]
for i in range(time):
    a.append(int(sys.stdin.readline()))

a.sort()

for i in a:
    print(i)
