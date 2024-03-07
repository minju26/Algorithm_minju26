import sys
input = sys.stdin.readline

n = int(input())
testCase = [int(input()) for _ in range(n)]
m = max(testCase)

dp_0 = [0]*(m+1)
dp_1 = [0]*(m+1)

for i in range(m+1):
    if i == 0:
        dp_0[i] = 1
    elif i == 1:
        dp_1[i] = 1
    else:
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]

for i in testCase:
    print(dp_0[i], dp_1[i])