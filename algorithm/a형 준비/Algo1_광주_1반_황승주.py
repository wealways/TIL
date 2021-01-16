# import sys
# sys.stdin = open('input1.txt')

from collections import deque
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    #1 bomb : 폭탄의 좌표와 크기
    bomb = deque()
    for _ in range(M):
        bomb.append((map(int,input().split())))
    #2 cnt : 피해수 체크
    cnt = 0
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    #3 폭탄 다 터질 때까지
    while bomb:
        r,c,v = bomb.popleft()
        #4 이미 떨어진 곳은 합산하지 않을 거에요.
        if data[r][c]>=0:
            cnt += data[r][c]
            data[r][c] = -1
        tempr,tempc = r,c
        #5 4방향으로 터지니까 반복
        for i in range(4):
            #6 폭탄의 크기만큼 한 방향으로 반복해줄거에요
            for _ in range(v):
                nr,nc = tempr+dr[i],tempc+dc[i]
                #7 지도의 범위
                if 0<=nr<N and 0<=nc<N:
                    #8 이미 떨어진 곳이 아니면, 카운트해주고요. 폭탄이 이미 떨어졌다고 체크해줄거에요.
                    if data[nr][nc]>=0:
                        cnt += data[nr][nc]
                        data[nr][nc]=-1
                    #9 폭탄크기만큼 반복해줘야하니까.
                    tempr,tempc = nr,nc
            #10 폭탄 크기만큼 반복이 끝났으면 원점에서 다시 다른 방향 체크
            tempr,tempc = r,c
    print('#{} {}'.format(tc,cnt))
