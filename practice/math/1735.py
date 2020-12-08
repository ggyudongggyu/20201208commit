from math import gcd
def lcm(x, y):
    return x*y // gcd(x,y)
def gcd(x, y):
    while y:
        x, y = y , x%y
    return x
a, aa = map(int, input().split())
b, bb = map(int, input().split())
if aa==bb:
    x = a+b
    y = gcd(x, aa)
    if y!=1:
        print(x//y, aa//y)
    else:
        print(x, aa)
else:
    x = lcm(aa, bb)
    y = a*x//aa + b*x//bb
    z =gcd(x,y)
    if z==1:
        print(y, x)
    else:
        print(y//z, x//z)
