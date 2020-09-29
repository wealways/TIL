import sys
sys.stdin = open('swea4615.txt','r')

T=int(input())

# 1==흑 / 2==백
for tc in range(1,T+1):
    dx=[1,1,1,0,-1,-1,-1,0]
    dy=[1,0,-1,-1,-1,0,1,1]

    N, M = map(int,input().split())

    board=[[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2

    for _ in range(M):
        x,y,a = map(int,input().split())
        x -= 1
        y -= 1
        board[y][x] = a
        for i in range(8):
            newx = x+dx[i]
            newy = y+dy[i]
            visit=[]
            while True:
                if not(0<=newx<N and 0<=newy<N) or (board[newy][newx]==0):
                    visit=[]
                    break
                if board[newy][newx]==a:
                    break

                visit.append((newy,newx))
                newy += dy[i]
                newx += dx[i]
            for newy, newx in visit:
                board[newy][newx]=a
    a,b=0,0
    for i in range(N):
        a += board[i].count(1)
        b += board[i].count(2)
    print(f'#{tc} {a} {b}')

