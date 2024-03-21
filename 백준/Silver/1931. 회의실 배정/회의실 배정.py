import sys

input = sys.stdin.readline

n = int(input())

timeList = []
answer = []

for _ in range(n):
    s, e = map(int, input().split())
    timeList.append((s, e))

timeList.sort(key= lambda x: (x[1], x[0]))
answer.append(timeList[0])

j = 0

for i in range(1, n):
    end = answer[j][1]
    if timeList[i][0] >= end:
        answer.append(timeList[i])
        j += 1

print(len(answer))