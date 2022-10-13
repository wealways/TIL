import sys
from collections import deque
sys.stdin = open("in5.txt")

N = int(input())

data = deque([])
for _ in range(N):
    data.append(input())

for _ in range(N-1):
    inputData = input()
    while True:
        tt = data.popleft()
        
        if inputData != tt:
            data.append(tt)
        else:
            break
print(data[0])
        