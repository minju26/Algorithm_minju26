import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

lcs = [[0] * (len(b) + 1) for _ in range((len(a) + 1))]

# lcs[0][c], lcs[r][0] = 0 으로 설정
# lcs[i][j] => a[i - 1], b[j - 1] 위치에서 비교 값을 저장
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

print(lcs[len(a)][len(b)])