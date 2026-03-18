import sys
import heapq

input = sys.stdin.read().split()
it = iter(input)

n = int(next(it))
m = int(next(it))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u = int(next(it))
    v = int(next(it))
    w = int(next(it))
    graph[u].append((v, w))

start = int(next(it))
end = int(next(it))

dist = [float('inf')] * (n + 1)
dist[start] = 0
pq = [(0, start)]

while pq:
    curr, u = heapq.heappop(pq)

    if dist[u] < curr:
        continue

    for v, weight in graph[u]:
        if curr + weight < dist[v]:
            dist[v] = curr + weight
            heapq.heappush(pq, (dist[v], v))

print(dist[end])
