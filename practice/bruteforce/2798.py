a, b = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
for i in range(0, len(c)-2):
    for j in range(i+1, (len(c)-1)):
        for k in range(j+1, (len(c))):
            V = c[i]+c[j]+c[k]
            if V > ans and V <= b:
                ans = V
print(ans)
