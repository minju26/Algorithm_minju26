# boj 15652 :: N과 M(4) :: silv.3

# 만약 M개를 전부 골랐다면, 조건에 맞는 탐색을 한 가지 성공한 것.
# 아직 M개를 고르지 않았다면, k번째부터 M번째 원소를 조건에 맞게 고르는 모든 방법 시도

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ans = []
selected = []

def recur(k):
    # m개를 모두 고른 경우
    if (k == m):
    	# 숫자 사이에 공백을 둔 문자열로 저장
        ans.append(' '.join(map(str, selected)))
        return
    else:
        # 앞 숫자보다 큰 수가 와야 하므로 다음에 올 수 있는 시작값을 설정
        if (k == 0): start = 1
        else: start = selected[k-1] + 1

        for i in range(start, n+1):
            selected.append(i)
            recur(k+1)
            selected.pop()	# 마지막 원소 제거

recur(0)
print('\n'.join(ans))