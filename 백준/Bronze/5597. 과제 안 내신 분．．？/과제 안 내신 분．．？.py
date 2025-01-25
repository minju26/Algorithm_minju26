check = [0] * 31

for i in range(28):
    n = int(input())
    check[n] = 1

ans = []
for i in range(1, 31):
    if check[i] == 0:
        ans.append(i)

print(ans[0])
print(ans[1])