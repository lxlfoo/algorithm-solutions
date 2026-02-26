import sys

s = sys.stdin.readline().strip()

cases = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        cases.add(s[i:j+1])

print(len(cases))
