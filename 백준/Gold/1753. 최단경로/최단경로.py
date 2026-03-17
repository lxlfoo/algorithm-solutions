import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
dist = [INF] * (v + 1)

for _ in range(e):
    u, b, w = map(int, input().split())
    graph[u].append((b, w))

q = []
heapq.heappush(q, (0, start))
dist[start] = 0

while q:
    d, now = heapq.heappop(q)

    if dist[now] < d:
        continue

    for i in graph[now]:
        cost = d + i[1]

        if cost < dist[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

for i in range(1, v + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
