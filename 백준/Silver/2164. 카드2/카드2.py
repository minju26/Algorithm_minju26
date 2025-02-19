import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    q.append(i)

while True:
    if len(q) == 1:
        break

    first = q.popleft()
    second = q.popleft()
    q.append(second)

print(q.pop() + 1)
