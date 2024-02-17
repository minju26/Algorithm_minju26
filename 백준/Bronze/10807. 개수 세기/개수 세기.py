import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
v = int(input())

print(array.count(v))