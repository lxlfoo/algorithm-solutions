import sys

input = sys.stdin.read().split()

n = int(input[0])
m = int(input[1])

unheard = set(input[2:2+n])
unseen = set(input[2+n:])

rst = sorted(list(unheard & unseen))
print(len(rst))

for n in rst:
    print(n)
