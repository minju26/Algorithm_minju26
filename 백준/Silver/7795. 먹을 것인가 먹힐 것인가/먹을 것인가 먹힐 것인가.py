import sys
input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    result = 0
    index_b = 0

    for index_a in range(n):
        while index_b < m and b[index_b] < a[index_a]:
            index_b += 1
        result += index_b  # 현재 index_b는 a[index_a]보다 작은 원소의 개수

    ans.append(result)

for result in ans:
    print(result)
