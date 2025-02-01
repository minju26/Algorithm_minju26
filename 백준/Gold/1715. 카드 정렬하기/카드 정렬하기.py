# boj 1715 :: 카드 정렬하기 :: gld.4

import sys
from queue import PriorityQueue

input = sys.stdin.readline
pq = PriorityQueue()
ans = 0

n = int(input())

for _ in range(n):
    card = int(input())
    pq.put(card)

while True:
    
    if pq.qsize() == 1:
        break
    
    min_val_1 = pq.get()
    min_val_2 = pq.get()

    new_val = min_val_1 + min_val_2
    ans += new_val

    pq.put(new_val)

print(ans)