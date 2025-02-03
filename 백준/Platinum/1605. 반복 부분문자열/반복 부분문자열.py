import sys
input = sys.stdin.readline

# 입력 & 정답
l = int(input())
s = input()
ans = 0

# 해시 값 준비(s의 길이 l에 따른, 31의 (l-1)거듭제곱 까지 준비)
mod = 1e9 + 7   # 해시 값 커짐 방지
po = [0] * l
po[0] = 1
for i in range(1, l):
    po[i] = po[i - 1] * 31 % mod

# 길이 이분 탐색 준비
start = 1
end = l - 1

while start <= end:
    mid = (start + end) // 2

    # 찾음 여부 flag
    found = False

    # 첫 부분 문자열(길이 mid)의 해시값 계산
    hash = 0
    for i in range(mid):
        hash *= 31
        hash %= mod

        hash += ord(s[i]) - ord('a') + 1
        hash %= mod

    # 이전 해시 값 저장을 위한 딕셔너리
    checked = {}
    for i in range(0, l - mid + 1):

        if hash in checked:
            for j in checked[hash]:
                if s[j : j + mid] == s[i : i + mid]:
                    found = True
                    break   # j for문 빠져나감
            checked[hash].append(i)

            if found:
                break   # i for문 빠져나감
        else:
            checked[hash] = [i]

        # 해시 업데이트
        largest = ord(s[i]) - ord('a') + 1      # 현재 부분 문자열의 첫 문자(제거)
        hash += mod - largest * po[mid - 1]
        hash %= mod
        # 부분 문자열의 마지막 문자 추가
        if i < l - mid:
            hash *= 31
            hash %= mod
            hash += ord(s[i + mid]) - ord('a') + 1
            hash %= mod

    # 부분 문자열 길이 업데이트
    if found:
        ans = mid   # 현재 찾은 길이 저장
        start = mid + 1     # 더 긴 길이 탐색
    else:
        end = mid - 1   # 더 짧은 길이 탐색

print(ans)