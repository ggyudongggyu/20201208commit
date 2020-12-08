import sys
n, m, k =map(int, sys.stdin.readline().split()) # == map(int, input().split())
table = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    table[x][y] = 1
    table[y][x] = 1

def DFS(table, start_point, history):
    history.append(start_point)
    for i in range(len(table[start_point])):
        if table[start_point][i] and i not in history:
            history = DFS(table, i, history)
    return history

def BFS(table, start_point):
    temporary = [start_point]
    history = [start_point]
    while temporary:
        now_point = temporary.pop(0)
        for i in range(len(table[start_point])):
            if table[now_point][i] and i not in history:
                temporary += [i]
                history += [i]
    return history

print(*DFS(table, k, []))
print(*BFS(table, k))