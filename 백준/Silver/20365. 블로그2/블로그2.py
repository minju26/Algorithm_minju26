import sys
input = sys.stdin.readline

n = int(input())
colors = input().strip()

new = now = colors[0]
for i in range(1, n):
    if colors[i] == now:
        continue
    else:
        new += colors[i]
        now = colors[i]

b = 0
r = 0
for c in new:
    if c == "B":
        b += 1
    else:
        r +=1

print(1 + min(b, r))