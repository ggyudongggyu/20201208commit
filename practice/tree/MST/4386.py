import math
import heapq
n = int(input())
a = []
distance = [[]for _ in range(n)]
for _ in range(n):
    x, y = map(float, input().split())
    a.append([x,y])
for i in range(n-1):
    for j in range(i, n):
        l = round(math.sqrt((a[i][0]-a[j][0])**2+(a[i][1]-a[j][1])**2),2)
        if i==j:
            continue
        distance[i].append([l, j])
        distance[j].append([l, i])

queue = []
heapq.heappush(queue, [0,0])

mst = 0
y = [0 for _ in range(n)]
while queue:
    l, destination = heapq.heappop(queue)
    if y[destination] == 1: continue
    mst += l
    y[destination] = 1
    for l, destination in distance[destination]:
        heapq.heappush(queue, [l, destination])
print(mst)
