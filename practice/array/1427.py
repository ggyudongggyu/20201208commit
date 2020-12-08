import sys

num = int(sys.stdin.readline())
a = []
while num > 0 :
    a.append(num%10)
    num = num // 10
a.sort()
a.reverse()
for i in range(len(a)):
    print(a[i], end='')
