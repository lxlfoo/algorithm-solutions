import sys

input = sys.stdin.readline
addr = input().strip()

if '::' in addr:
    slices = addr.split('::')
    left = slices[0].split(':') if slices[0] else []
    right = slices[1].split(':') if slices[1] else []

    count = 8 - (len(left) + len(right))
    blocks = left + ['0000'] * count + right
else:
    blocks = addr.split(':')

result = []
for b in blocks:
    result.append(b.zfill(4))

print(':'.join(result))
