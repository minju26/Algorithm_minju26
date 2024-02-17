import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
v = int(input())

cnt = 0

for num in array:
    if num == v: cnt+=1

print(cnt)