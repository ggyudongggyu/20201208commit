n=int(input()) #컴퓨터 수 n
m=int(input())
mat = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    link = list(map(int, input().split()))
    mat[link[0]][link[1]] = 1
    mat[link[1]][link[0]] = 1

def dfsdfs(now_node, r, save):
    save += [now_node]
    for next_node in range(len(r[now_node])):
        if r[now_node][next_node] and next_node not in save:
            save = dfsdfs(next_node, r, save)
    return save

ans = len(dfsdfs(1, mat, []))
print(ans-1)
