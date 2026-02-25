import sys

input = sys.stdin.readline

def distance(a, b):
    dist = 0
    for i in range(4):
        if a[i] != b[i]:
            dist += 1
    return dist

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()

    if n > 32:
        print(0)
    else:
        ans = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    d = distance(mbti[i], mbti[j]) + distance(mbti[j], mbti[k]) + distance(mbti[i], mbti[k])
                    ans = min(ans, d)

        print(ans)
