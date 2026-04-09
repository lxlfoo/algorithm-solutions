import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

min_dist = float('inf')

for open_chickens in combinations(chickens, m):
    city_dist = 0

    for hr, hc in houses:
        temp_dist = float('inf')
        for cr, cc in open_chickens:
            dist = abs(hr - cr) + abs(hc - cc)
            temp_dist = min(temp_dist, dist)

        city_dist += temp_dist

        if city_dist >= min_dist:
            break

    min_dist = min(min_dist, city_dist)

print(min_dist)
