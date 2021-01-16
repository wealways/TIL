# import sys
# sys.stdin = open('input2.txt')

def find(r,c,cnt):
    global flag,answer
    # 벽이 있으면 뚫었다고 체크
    if data[r][c]==1:
        flag +=1
    # 벽을 두번 이상 뚫으면 되돌아가기
    if flag ==2:
        return

    # 도착지점 나오면 최소값 반환
    if data[r][c]==3:
        answer = min(answer,cnt)
        flag=0
        return
    else:
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            # 범위 체크
            if 0<=nr<N and 0<=nc<N:
                # 방문 안했고 벽 두번 안 뚫었으면
                if (nr,nc) not in visit and flag < 2:
                    visit.append((nr,nc))
                    find(nr,nc,cnt+1)
                    # 이전 값이 벽이여서 리턴되었으면 벽 뚫었던 거 되돌아가기
                    if data[nr][nc]==1 and flag>0 :
                        flag -=1
                    visit.pop()



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [[int(i) for i in list(input())] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j]==2:
                sr,sc = i,j
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    # 벽을 뚫었는 지 체크
    flag = 0
    # 초기값 설정
    answer = float('inf')
    cnt = 1
    # 방문여부 체크
    visit = []
    visit.append((sr,sc))
    find(sr, sc, 1)

    # 도착지점까지 못갔다는 것이기 때문에 답을 0으로 설정
    if answer == float('inf'): answer=0
    print('#{} {}'.format(tc,answer))
