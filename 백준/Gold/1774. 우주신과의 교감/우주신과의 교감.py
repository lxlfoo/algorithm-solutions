import sys

input = sys.stdin.readline

def find(p, x):
    if p[x] != x: p[x] = find(p, p[x])
    return p[x]

n, m = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]
parent = list(range(n))

edges_count = 0
for _ in range(m):
    u, v = map(int, input().split())
    if find(parent, u-1) != find(parent, v-1):
        parent[find(parent, u-1)] = find(parent, v-1)
        edges_count += 1

candidates = []
for i in range(n):
    for j in range(i + 1, n):
        d = ((pos[i][0]-pos[j][0])**2 + (pos[i][1]-pos[j][1])**2)**0.5
        candidates.append((d, i, j))

candidates.sort()

ans = 0.0
for d, u, v in candidates:
    root_u, root_v = find(parent, u), find(parent, v)
    if root_u != root_v:
        parent[root_u] = root_v
        ans += d
        edges_count += 1
        if edges_count == n - 1: break

print(f"{ans:.2f}")
