import sys
sys.stdin = open('swea4875.txt', 'r')

T = int(input())

def chk(y,x):
    global ans

    miro[y][x]='2'
    for i in range(4):
        newx = x+dx[i]
        newy = y+dy[i]
        if 0<=newx < N and 0<= newy<N :
            if miro[newy][newx] == '3':
                ans = 1
                return True
            if miro[newy][newx]=='0':
                t = chk(newy,newx)
                if t:
                    return True
                # else:
                #     continue
    return False

for tc in range(1,T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    ans = 0
    for y in range(N):
        for x in range(N):
            if miro[y][x]=='2':
                startx, starty = x,y
                chk(starty,startx)
    print(f'#{tc} {ans}')