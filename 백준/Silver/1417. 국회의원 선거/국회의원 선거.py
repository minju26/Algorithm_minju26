import sys
from queue import PriorityQueue

input = sys.stdin.readline
pq = PriorityQueue()  

n = int(input())
p = [0] * n

for i in range(n):
    p[i] = int(input())

for i in range(1, n):
    pq.put(-p[i]) # 최대 -> 최소로 변환

if n == 1:
    print(0)
else:
    cnt = 0
    while True:
        max_val = -pq.get()
        if max_val < p[0]:
            break
        
        max_val -= 1
        p[0] += 1
        cnt +=1
        pq.put(-max_val)
    
    print(cnt)