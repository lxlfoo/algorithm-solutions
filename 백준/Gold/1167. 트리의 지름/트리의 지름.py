import sys
from collections import deque

input = sys.stdin.readline
V = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(V):
    line = list(map(int, input().split()))
    u = line[0]
    for i in range(1, len(line) - 1, 2):
        v, w = line[i], line[i+1]
        graph[u].append((v, w))

def bfs(start):
    dist = [-1] * (V + 1)
    queue = deque([start])
    dist[start] = 0

    dist_max = 0
    end = start

    while queue:
        curr = queue.popleft()

        for neighbor, weight in graph[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + weight
                queue.append(neighbor)

                if dist[neighbor] > dist_max:
                    dist_max = dist[neighbor]
                    end = neighbor

    return end, dist_max

a, _ = bfs(1)
_, d = bfs(a)

print(d)
