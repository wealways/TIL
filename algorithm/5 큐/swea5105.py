import sys
sys.stdin = open('swea5105.txt','r')
dx=[0,0,1,-1]
dy=[1,-1,0,0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                start=(i,j)
            elif maze[i][j]=='3':
                end=(i,j)
    visit=[[0]*N for _ in range(N)]
    Q=[start]
    visit[start[0]][start[1]]=1
    while Q:
        x,y = Q.pop(0)
        if x==end[0] and y==end[1]:
            break
        for i in range(4):
            newx, newy = x+dx[i],y+dy[i]
            if 0<= newx < N and 0<=newy<N:
               if maze[newx][newy]!='1' and visit[newx][newy]==0:
                   visit[newx][newy]=visit[x][y]+1
                   Q.append((newx,newy))

    if visit[end[0]][end[1]]: visit[end[0]][end[1]]-=2
    print(visit[end[0]][end[1]])