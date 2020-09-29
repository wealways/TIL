import sys
sys.stdin = open('swea_2805.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    input_list = [list(map(int,list(input()))) for _ in range(N)]

    ans = 0
    s=N//2
    for i in range(N):
        ans += sum(input_list[i][abs(s-i):N-abs(s-i)])

    print('#{} {}'.format(tc,ans))