import heapq
import sys

N = int(input())
M = int(input())
li = [[]for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    li[a].append((b,c))
INF = 100001 * N
start , end = map(int, sys.stdin.readline().split())
cost_map = [INF] * (N+1)
cost_map[start] = 0
queue = []
heapq.heappush(queue, (start, 0))
while queue :
    now_city, cost = heapq.heappop(queue)

    for next_city, x in li[now_city]:
        expense = x + cost
        if expense < cost_map[next_city]:
            cost_map[next_city] = expense
            heapq.heappush(queue, (next_city, expense))

print(cost_map[end])