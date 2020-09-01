import sys
sys.stdin = open('2001.txt','r')



def chk(arr,curx,cury,m):

    result = 0
    for i in range(curx,curx+m):
        for j in range(cury,cury+m):
            result += arr[i][j]
    return result


T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    input_list = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    for curx in range(0,N-M+1):
        for cury in range(0,N-M+1):
            if result <= chk(input_list, curx, cury, M):
                result = chk(input_list, curx, cury, M)

    print('#{} {}'.format(tc,result))
