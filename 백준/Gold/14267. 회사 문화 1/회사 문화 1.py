import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = list(map(int, input().split()))

# 인덱스 = id 맞춰주기
for i in range(n):
    parents[i] -= 1

good = [0] * n
for _ in range(m):
    id, score = map(int, input().split())
    # 직속 상사로부터 칭찬을 받은 직원의 칭찬 수치 저장
    good[id-1] += score


total_good = [0] * n
for i in range(n):
    # 나의 총 칭찬 수치 = 나의 칭찬 수치(직속 상사로 부터 받은 것) + 나의 직속 상사의 총 칭찬 수치
    total_good[i] = good[i] + total_good[parents[i]]

print(*total_good)