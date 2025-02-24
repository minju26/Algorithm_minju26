# q^2 >= n 인 q값 찾기
import sys

input = sys.stdin.readline

n = int(input())

start = 0
# end = 2 ** 63 => n의 최대 값이 2**63 인데, 제곱근을 구하는 것이므로 가능한 최대 q값은 대략 2 ** 32 정도로 설정해도 된다.
end = 2 ** 32

ans = 0
while start <= end:
    mid = (start + end) // 2

    if (mid ** 2) >= n:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
