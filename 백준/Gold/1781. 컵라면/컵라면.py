import sys
import heapq

n = int(sys.stdin.readline())

dr_input = []
q = []

for _ in range(n):
    dline, rnum = map(int, input().split())
    dr_input.append((dline, rnum))

dr_input.sort()

for dr in dr_input:
    heapq.heappush(q, dr[1])
    if dr[0] < len(q):
        heapq.heappop(q)


print(sum(q))