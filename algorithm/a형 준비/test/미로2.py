T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [[int(x) for x in input()] for _ in range(N)]

    # 스타트 위치 찾기 2
    start = False
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i,j)
                break
        if start:
            break

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    Q = [start]
    visit = [[0]*N for _ in range(N)]

    x, y = start
    visit[x][y] = 1
    result = 0
    while Q:
        x, y = Q.pop(0)
        if miro[x][y] == 3:
            result = visit[x][y]
            break

        for i in range(4):
            newx, newy = x+dx[i], y+dy[i]
            if 0<= newx < N and 0<= newy < N:
                if (miro[newx][newy]==0 or miro[newx][newy]==3) and visit[newx][newy]==0:
                    Q.append((newx,newy))
                    visit[newx][newy] = visit[x][y] + 1
    if result >0:
        result -=2
    print('#{} {}'.format(tc,result))