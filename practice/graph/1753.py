import heapq
import sys

n, e = map(int, sys.stdin.readline().split())
s = int(input())
a = [[]for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    a[u].append((w, v))
INF = 10 * n + 1
d = [INF] * (n+1)
d[s] = 0
queue = []
heapq.heappush(queue, (0,s))
while queue:
    cost, now = heapq.heappop(queue)

    for x, next_node in a[now]:
        xc = x + cost
        if xc < d[next_node]:
            d[next_node] = xc
            heapq.heappush(queue, (xc, next_node))

for i in range(1, n+1):
    if d[i]==INF:
        print('INF')
    else: print(d[i])
