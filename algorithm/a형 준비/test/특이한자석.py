import sys
from collections import deque

sys.stdin = open('특이한자석.txt','r')

from collections import deque
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    magnet = [ deque(list(map(int,input().split()))) for _ in range(4)]
    '''
    - - v - - - V -
    0 0 1 0 0 1 0 0
    1 0 0 1 1 1 0 1
    0 0 1 0 1 1 0 0
    0 0 1 0 1 1 0 1
    1 시계방향 -1 반시계방향
    '''

    for n in range(N):
        idx,flag = map(int,input().split())
        # idx 0,1,2,3
        idx -= 1
        move = [(idx,flag)]

        # 왼쪽 자석이 움직일 때 붙어있는 왼쪽 자석도 움직입니다.
        temp = flag
        for i in range(idx-1,-1, -1):
            if magnet[i][2] != magnet[i+1][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 오른쪽 자석이 움직일 때 붙어있는 오른쪽 자석들도 움직입니다.
        temp = flag
        for i in range(idx+1, 4):
            if magnet[i-1][2] != magnet[i][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        for idx, flag in move:
            if flag == 1:
                magnet[idx].rotate(1)
            elif flag == -1:
                magnet[idx].rotate(-1)
    result = 0
    #1,2,4,8 / n극 0 : s극 1
    for i in range(4):
        result += magnet[i][0] * 2 ** i
    print('#{} {}'.format(tc, result))

