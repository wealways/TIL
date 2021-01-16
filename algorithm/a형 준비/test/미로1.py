# 1 stack 이용하기
def chk():
    global ans
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    start=False
    for x in range(N):
        for y in range(N):
            if miro[x][y] >= 2:
                start = (x,y)
                break
        if start != False:
            break

    s = [start]
    while s:
        x,y = s.pop(-1)
        miro[x][y] = 1
        for i in range(4):
            newx, newy = x+dx[i], y+dy[i]
            if 0 <= newx < N and 0 <= newy < N:
                if miro[newx][newy] >=2:
                    ans = 1
                    return
                if miro[newx][newy] == 0:
                    s.append((newx,newy))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [[int(x) for x in input()] for _ in range(N)]
    ans = 0
    chk()
    print('#{} {}'.format(tc,ans))

# 재귀이용하기
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
                return
            if miro[newy][newx]=='0':
                chk(newy,newx)

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