def det_num(n):
    sum = n
    while True:
        if n<=0:
            break
        sum = sum + (n%10)
        n = n // 10
    return sum

a = int(input())
ans = 0
for i in range(1,a):
    if a == det_num(i):
        ans = i
        break
print(ans)
