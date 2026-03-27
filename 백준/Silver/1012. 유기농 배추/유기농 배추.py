import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, m, n, graph):
    queue = deque([(x, y)])
    graph[y][x] = 0

    while queue:
        x_curr, y_curr = queue.popleft()

        for i in range(4):
            nx = x_curr + dx[i]
            ny = y_curr + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                bfs(i, j, m, n, graph)
                count += 1
    print(count)
