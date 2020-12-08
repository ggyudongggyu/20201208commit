import sys
import heapq

case = int(input())
max_heap = []
min_heap = []

for _ in range(case):
    x = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)
    if min_heap and -max_heap[0] > min_heap[0]:
        i, j = heapq.heappop(min_heap), -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -i)
        heapq.heappush(min_heap, j)
    print(-max_heap[0])
