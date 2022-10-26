import sys
from collections import deque
sys.stdin = open("in{}.txt".format(5))
arr = [list(map(int,input().split())) for _ in range(7)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

q = deque([])
q.append((0,0,0))
arr[0][0] = 1

answer = -1
while q:
    x,y,cnt=q.popleft()
    if x==6 and y==6:
        answer = cnt
        break
    for i in range(4):
        tempx = x+dx[i]
        tempy = y+dy[i]
        if 0<=tempx<7 and 0<=tempy<7 and arr[tempx][tempy] == 0:
            q.append((tempx,tempy,cnt+1))
            arr[tempx][tempy] = 1

print(answer)