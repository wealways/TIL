import sys
sys.stdin = open('4613.txt','r')

T = int(input())


for tc in range(1,T+1):
    N, M = map(int, input().split())
    input_list = [list(input()) for _ in range(N)]
    w = [0]*N
    B = [0] * N
    R = [0] * N
    for i in range(N):
        for j in range(M):
            if input_list[i][j] != 'W':
                w[i] +=1
            if input_list[i][j] != 'B':
                B[i] +=1
            if input_list[i][j] != 'R':
                R[i] +=1
    for i in range(1,N):
        w[i] += w[i-1]
        B[i] += B[i-1]
        R[i] += R[i - 1]
    MinV = N*M
    for i in range(N-2):
        for j in range(i-1,N-1):
            s1 = w[i]
            s2 = B[j]-B[i]
            s3 = R[N-1] - R[j]
            if MinV >s1+s2+s3:
                MinV = s1+s2+s3
    print('#{} {}'.format(tc,MinV))