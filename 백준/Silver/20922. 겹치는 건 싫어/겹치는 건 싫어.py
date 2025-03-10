import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = {}
left = 0
max_length = 0  

for right in range(n):  
    num = a[right]
    count[num] = count.get(num, 0) + 1  

    while count[num] > k:
        count[a[left]] -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
