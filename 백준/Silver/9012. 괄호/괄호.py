import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    vps = input().strip()
    stack = list()
    flag = True

    for c in vps:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                flag = False
                break
            stack.pop()

    if flag and not stack:
        print('YES')
    else:
        print('NO')
