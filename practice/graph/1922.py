def find(n): #n으로 들어온 원소의 Root노드를 반환
    if p[n] == n :
        return n
    else:
        x = find(p[n])
        p[n] = x
        return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x!=y:
        p[y] = x

N = int(input()) #정점
M = int(input()) #간선
graph = []
for _ in range(M):
    a, b, c = map(int,input().split())
    graph.append([a,b,c])
graph.sort(key=lambda x:x[2])
rank = [0 for _ in range(N+1)]
p = [i for i in range(N+1)]
cost = 0
node_count = 0
for i in range(M):
    u = graph[i][0]
    v = graph[i][1]
    r = graph[i][2]
    if find(u)!=find(v):
        union(u, v)
        cost += r
        node_count += 1
    if node_count==N-1:
        break
print(cost)
print(p)
