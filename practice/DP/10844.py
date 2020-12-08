n = int(input())
p = [[1]*12]
p[0][0] = p[0][-1] = p[0][1] = 0
for i in range(1,n):
    p.append([0]*12)
    for j in range(1, 11):
        p[i][j] = p[i-1][j-1] + p[i-1][j+1]
print(sum(p[-1])%1000000000)
