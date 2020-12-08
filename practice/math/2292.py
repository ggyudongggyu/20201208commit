N = int(input())
n = 0
while True:
    n = n+1
    if N < 3*(n**2) - 3*n + 2:
        break
print(n)
