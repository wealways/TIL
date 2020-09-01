import sys
sys.stdin = open('4836.txt','r')

T = int(input())

for tc in range(1,T+1):

    temp_list=[[0]*10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        a,b,c,d,T = map(int,input().split())
        cnt = 0
        for i in range(a,c+1):
            for j in range(b,d+1):
                temp_list[i][j] += T
    for i in range(10):
        for j in range(10):
            if temp_list[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc,cnt))