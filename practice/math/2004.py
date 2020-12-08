n , r = map(int, input().split())
rr = n-r

def five(x):
    y = x//5
    x //= 5
    while x>4:
        x //= 5
        y += x
    return y
def two(x):
    y = x//2
    x //= 2
    while x>1:
        x //= 2
        y += x
    return y

a = five(n)-five(r)-five(rr)
b = two(n)-two(r)-two(rr)
print(min(a,b))
