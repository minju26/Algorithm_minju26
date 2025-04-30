import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = 0
for _ in range(n):
    hw = input().strip()

    if hw != '0':
        op, score, min = map(int, hw.split())
        min -= 1

        if min == 0:
            ans += score
        else:
            stack.append([score, min])
    else:
        if len(stack) == 0: continue
        
        score, min = stack[-1]
        min -= 1

        if min == 0:
            ans += score
            stack.pop()
        else:
            stack[-1][1] = min

print(ans)
