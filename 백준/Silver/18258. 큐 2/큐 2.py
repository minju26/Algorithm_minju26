from collections import deque
import sys

n = int(input())
d = deque()

for i in range(n):
    command = sys.stdin.readline()
    command = command.split()

    if command[0] == "push":
        d.append(command[1])

    if command[0] == "pop":
        if len(d) == 0:
            print("-1")
        else:
            print(d.popleft())
        
    if command[0] == "size":
        print(len(d))
    
    if command[0] == "empty":
        if len(d) == 0:
            print("1")
        else:
            print("0")
    
    if command[0] == "front":
        if len(d) == 0:
            print("-1")
        else:
            print(d[0])
    
    if command[0] == "back":
        if len(d) == 0:
            print("-1")
        else:
            print(d[-1])
