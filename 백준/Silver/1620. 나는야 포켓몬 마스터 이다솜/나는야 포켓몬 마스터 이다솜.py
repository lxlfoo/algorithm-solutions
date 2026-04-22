import sys

input = sys.stdin.readline
n, m = map(int, input().split())

pokedex = [''] * (n + 1)
num = {}

for i in range(1, n + 1):
    name = input().strip()
    pokedex[i] = name
    num[name] = i

results = []
for _ in range(m):
    query = input().strip()

    if query.isdigit():
        results.append(pokedex[int(query)])
    else:
        results.append(str(num[query]))

print('\n'.join(results))
