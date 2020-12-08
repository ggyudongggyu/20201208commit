def find(x):
    if p[x]==x:
        return x
    else:
        y = find(p[x])
        p[x] = y
        return y

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        if rank[x] > rank[y]:
            p[y]=x
        else:
            p[x]=y
            if rank[x]==rank[y]:
                rank[y]+=1


v, e = map(int, input().split())
graph = []
rank = [0 for _ in range(v+1)]
p = [i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([c,a,b])

graph.sort(key=lambda x:x[0])
e_count = 0
mst = 0
for i in range(e):
    r = graph[i][0]
    pp = graph[i][1]
    qq = graph[i][2]
    if find(pp) != find(qq):
        union(pp, qq)
        mst += r
        e_count += 1
    if e_count==v-1:
        break
print(mst)
