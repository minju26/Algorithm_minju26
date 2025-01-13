# boj 11728 :: 배열 합치기 :: silv.5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a + b
c.sort()

print(*c)