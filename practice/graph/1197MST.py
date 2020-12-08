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
    if x!=y:  #짧은 트리의 루트가 긴 트리의 루트를 가리키게 하는 것이 좋음.
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
cnt = 0
for i in range(e):
    r = graph[i][0] #가중치
    pp = graph[i][1]
    qq = graph[i][2] #pp,qq는 간선으로 이어져있음.
    if find(pp) != find(qq): #이어져있는데 find값이 다르면 안되니까
        union(pp, qq) #혹시 다르면 union함수 통해서 같게 만들어주기
        cnt += r
        e_count += 1
    if e_count==v-1: #모든 정점이 연결됐다면 스탑.
        break
print(cnt)
