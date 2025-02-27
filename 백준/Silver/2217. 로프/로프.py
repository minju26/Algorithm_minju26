import sys

input = sys.stdin.readline

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))
rope.sort()

ans = rope[0] * n
for i in range(1, n):
    if rope[i] == rope[i - 1]:
        continue

    ans = max(ans, rope[i] * (n - i))

print(ans)