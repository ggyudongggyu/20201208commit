import heapq
from sys import stdin

n = int(stdin.readline())
list = []

for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        if list:
            print(heapq.heappop(list)[1])
        else:
            print(0)
    else:
        heapq.heappush(list, [-x, x])
