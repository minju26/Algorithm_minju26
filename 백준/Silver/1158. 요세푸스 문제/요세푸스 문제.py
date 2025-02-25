import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([])
result = []

for i in range(n):
    q.append(i + 1)

while len(q) != 0:

    for _ in range(k -1):
        x = q.popleft()
        q.append(x)
    
    out = q.popleft()
    result.append(out)

ans = "<" + ", ".join(map(str, result)) + ">"
print(ans)