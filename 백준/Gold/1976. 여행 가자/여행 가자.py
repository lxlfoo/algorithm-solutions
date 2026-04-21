import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    road = list(map(int, input().split()))
    for j in range(1, n + 1):
        if road[j-1] == 1:
            union(parent, i, j)

trip = list(map(int, input().split()))

rst = "YES"
if m > 0:
    root = find(parent, trip[0])
    for i in range(1, m):
        if find(parent, trip[i]) != root:
            rst = "NO"
            break

print(rst)
