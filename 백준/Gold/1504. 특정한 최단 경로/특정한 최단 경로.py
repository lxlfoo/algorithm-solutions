import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n, e = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())

def solve(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, curr = heapq.heappop(pq)
        if dist[curr] < d: continue
        for next, weight in adj[curr]:
            if dist[next] > d + weight:
                dist[next] = d + weight
                heapq.heappush(pq, (dist[next], next))
    return dist

d1 = solve(1)
s1 = solve(v1)
s2 = solve(v2)

rst = min(d1[v1] + s1[v2] + s2[n], d1[v2] + s2[v1] + s1[n])
print(rst if rst < INF else -1)
