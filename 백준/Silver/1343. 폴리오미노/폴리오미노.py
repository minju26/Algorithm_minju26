# "X" 4개를 모으면 "AAAA"로 대체(그리디), "."이 나타났을 때의 "X" 개수에 따라 다르게 처리
import sys
input = sys.stdin.readline

board = input().strip()
ans = ""

x_cnt = 0
possible = True
for i in range(len(board)):
    if board[i] == "X":
        x_cnt += 1
        if x_cnt == 4:
            ans += "AAAA"
            x_cnt = 0
    else:
        if x_cnt == 0:
            ans += "."
        elif x_cnt == 1:
            possible = False
            break
        elif x_cnt == 2:
            ans += "BB"
            ans += "."
            x_cnt = 0
        elif x_cnt == 3:
            possible = False
            break

if x_cnt == 1:
    possible = False
elif x_cnt == 2:
    ans += "BB"
elif x_cnt == 3:
    possible = False

if possible:
    print(ans)
else:
    print(-1)