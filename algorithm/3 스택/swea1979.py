import sys
sys.stdin = open('swea1979.txt','r')

def chk(x,y):
    visited[x][y]=1


T= int(input())
for tc in range(1,11):
    N,K =map(int,input().split())
    input_list=[list(map(int,input().split())) for _ in range(N)]
    trans = list(map(list, zip(*input_list)))
    totalcnt = 0
    # 가로 테스트
    for idx in range(N):
        i = 0

        while i <N:
            cnt = 0
            while i < N and input_list[idx][i]==0:
                i+=1
            while i < N and input_list[idx][i] == 1:
                i+=1
                cnt += 1
            if cnt==K:
                totalcnt += 1

    #세로 테스트
    for idx in range(N):
        i = 0

        while i <N:
            cnt = 0
            while i < N and trans[idx][i]==0:
                i+=1
            while i < N and  trans[idx][i] == 1:
                i+=1
                cnt += 1
            if cnt==K:
                totalcnt += 1

    print(f'#{tc} {totalcnt}')