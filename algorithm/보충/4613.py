'''
    w b r
    3 0 2  -> 2
    2 2 1  - 3 / 3
    3 0 2  - 5 / 3
    2 1 2  -> 3

    ----
    w   b   r
    14  0   0  -> 14
    6   6   2  -> 8 / 8
    8   2   4  ->
    7   3   4
    7   5   2
    14  0   0  -> 14

    '''
import sys
sys.stdin = open('4613.txt','r')

T = int(input())
T=2

for tc in range(1,T+1):
    N, M = map(int, input().split())
    input_list = [list(input()) for _ in range(N)]

    # n 하얀색 줄 개수 / m 빨간색 줄 갯수
    n = 1
    m = 1

    result = N*M
    w_cnt=0
    for i in range(0,N-2):
        for j in range(0,M):
            if input_list[i][j]!='W':
                w_cnt += 1

        b_cnt = 0
        for a in range(i+1,N-1):
            for b in range(0,M):
                if input_list[a][b] !='B':
                    b_cnt += 1

            r_cnt = 0
            for c in range(a+1,N):
                for d in range(0,M):
                    if input_list[c][d] != 'R':
                        r_cnt += 1

            cnt = w_cnt + b_cnt + r_cnt
            if result >= cnt:
                result = cnt

    print(result)

