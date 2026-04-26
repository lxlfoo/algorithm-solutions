import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

while True:
    try:
        line = input().split()
        if not line: break
        m, n = map(int, line)
    except ValueError:
        break

    if m == 0 and n == 0:
        break

    edges = []
    total_cost = 0
    for _ in range(n):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        total_cost += w

    edges.sort()
    parent = list(range(m))
    mst_cost = 0
    count = 0

    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_cost += w
            count += 1
            if count == m - 1:
                break

    print(total_cost - mst_cost)
