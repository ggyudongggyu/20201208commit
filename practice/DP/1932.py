n=int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, len(p)):
    p[i][0] = p[i][0] + p[i-1][0]
    p[i][i] = p[i][i] + p[i-1][i-1]
    for j in range(1, len(p[i])-1):
        p[i][j] = p[i][j] + max(p[i-1][j-1], p[i-1][j])

print(max(p[-1]))
