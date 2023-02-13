import sys, heapq

n = int(sys.stdin.readline())

time_list = []

for i in range(n):
    st, et = map(int, sys.stdin.readline().split())
    time_list.append([st, et])

time_list.sort()

queue = []
heapq.heappush(queue, time_list[0][1])


for i in range(1,n):
    if time_list[i][0] < queue[0]:
        heapq.heappush(queue, time_list[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, time_list[i][1])

print(len(queue))
