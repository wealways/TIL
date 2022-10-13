import sys
from collections import deque

sys.stdin = open("in1.txt")

inputData = list(input())
for _ in range(int(input())):
    subject = list(input())
    essential = deque(inputData)
    
    for s in subject:
        if essential and s == essential[0]:
            essential.popleft()
    if essential:
        print('NO')
    else:
        print('YES')

