import sys
from itertools import combinations

input = sys.stdin.readline
n, k = map(int, input().split())

words = []
for _ in range(n):
    words.append(input().strip()[4 : -4])

if k < 5:
    print(0)
else:    
    def check(words, learned):
        cnt = 0
        for word in words:
            checked = True
            for w in word:
                if not learned[ord(w) - ord('a')]:
                    checked = False
                    break
            if checked:
                cnt += 1
        return cnt
    
    alpha = []
    antatica = ['a', 'c', 'i', 'n', 't']
    for i in range(26):
        if chr(ord('a') + i) in antatica:
            continue
        alpha.append(chr(ord('a') + i))
    
    learned = [False] * 26
    for x in antatica:
        learned[ord(x) - ord('a')] = True

    ans = 0
    for com in combinations(alpha, k - 5):
        for x in com:
            learned[ord(x) - ord('a')] = True

        cnt = check(words, learned)
        ans = max(ans, cnt)

        for x in com:
            learned[ord(x) - ord('a')] = False

    print(ans)