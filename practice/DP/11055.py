n = int(input())
a = list(map(int, input().split()))
b = [0]*n
b[0] = a[0]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            b[i] = max(a[i] + b[j], b[i])
    if not b[i]:
        b[i] = a[i]

print(max(b))
