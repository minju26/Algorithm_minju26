import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    num = int(input())

    if num != 0:
        stack.append(num)
    if num == 0:
        stack.pop()

print(sum(stack))
