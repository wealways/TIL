import sys
from collections import deque
sys.stdin = open("in{}.txt".format(2))

N = int(input())

apples = [list(map(int,input().split())) for _ in range(N)]

q= deque([])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q.append([N//2,N//2,0])
answer = apples[N//2][N//2]
visit = [[N//2,N//2]]


while q:
    x,y,cnt = q.popleft()
    if cnt ==N//2:
        break
    for i in range(4):
        tempx = x+dx[i]
        tempy = y+dy[i]
        if 0<=tempx<N and 0<=tempy<N and [tempx,tempy] not in visit:
            q.append([tempx,tempy,cnt+1])
            answer += apples[tempx][tempy]
            visit.append([tempx,tempy])
    
print(answer)