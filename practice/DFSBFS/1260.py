N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


print(*dfs(V, matrix, []))
print(*bfs(V))


# from collections import deque
#
# v, e, s = map(int, input().split())
# a = [[0 for _ in range(v+1)] for _ in range(v+1)]
#
# for _ in range(e):
#     x, y = map(int, input().split())
#     a[x][y], a[y][x] = 1,1
#
# def dfs(a, s, result):
#     result += [s]
#     for i in range(1, v+1):
#         if a[s][i] and i not in result:
#             result = dfs(a, i, result)
#     return result
#
# print(*dfs(a, s, []))
#
# def bfs(s):
#     queue = deque([s])
#     result = [s]
#     while queue:
#         s = queue.popleft()
#         for i in range(1, v+1):
#             if a[s][i] and i not in result:
#                 result += [i]
#                 queue.append(i)
#     return result
# print(*bfs(s))
