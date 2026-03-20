import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def solve(start, adj, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d: continue
        for v, w in adj[now]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(q, (dist[v], v))
    return dist

n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph1[u].append((v, w))
    graph2[v].append((u, w))

rst1 = solve(x, graph1, n)
rst2 = solve(x, graph2, n)
print(max(rst1[i] + rst2[i] for i in range(1, n+1) if rst1[i] < INF))
