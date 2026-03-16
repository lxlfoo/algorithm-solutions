import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

dist = [-1] * (n + 1)
dist[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()

    if dist[now] == k:
        continue

    for next in graph[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            queue.append(next)

found = False
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
