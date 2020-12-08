N, M = map(int, input().split())
out = []
result=[]
def solve(depth, idx, N, M):
    if depth == M:
        result.append(out[:])
        return 
    for i in range(idx, N):
        out.append(i+1)
        solve(depth+1, i, N, M)
        out.pop()

solve(0, 0, N, M)
for i in result:
    print(*i)