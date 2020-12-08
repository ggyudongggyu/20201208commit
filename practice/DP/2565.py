f = []
N = int(input())
for i in range(N):
    f.append(list(map(int, input().split())))
f = sorted(f, key = lambda x: (x[0], x[1]))

B = [0] * N
for i in range(N):
    for j in range(0,i):
        if f[i][1] > f[j][1] and B[i] < B[j]:
            B[i] = B[j]
    B[i]+=1
print(N - max(B))
