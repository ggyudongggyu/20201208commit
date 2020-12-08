n, m = map(int, input().split())
mm = n-m
x, y = max(m,mm), min(m,mm)
c1 = c2 = 1
for i in range(n, x, -1):
    c1 *= i
for i in range(1, y+1):
    c2 *= i
print(c1//c2)
