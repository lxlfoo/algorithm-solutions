import sys

input = sys.stdin.readline

target = input().strip()
bomb = input().strip()

bomb_len = len(bomb)
c = bomb[-1]
stack = []

for char in target:
    stack.append(char)

    if char == c and len(stack) >= bomb_len:
        if ''.join(stack[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                stack.pop()

result = ''.join(stack)
print(result if result else 'FRULA')
