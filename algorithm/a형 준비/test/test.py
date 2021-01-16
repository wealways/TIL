from collections import deque
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    magnet = [deque(list(map(int, input().split()))) for _ in range(M)]
    '''
    - - v - - - V -
    0 0 1 0 0 1 0 0
    1 0 0 1 1 1 0 1
    0 0 1 0 1 1 0 0
    0 0 1 0 1 1 0 1
    1 시계방향 -1 반시계방향
    '''

    for n in range(N):
        idx, flag = map(int, input().split())
        # idx 0,1,2,3
        idx -= 1
        move = [(idx, flag)]

        temp = flag
        for i in range(idx - 1, -1, -1):
            ## 새로운 방식
            # 날의 수는 항상 4의 배수라고 했기 때문에 4로 나눠주면 자석끼리 만나는 점을 확인할 수 있다.
            a = len(magnet[i])//4
            b = len(magnet[i+1])//4
            if magnet[i][a] != magnet[i + 1][b*3]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        temp = flag
        for i in range(idx + 1, 3):
            ## 새로운 방식
            # 날의 수는 항상 4의 배수라고 했기 때문에 4로 나눠주면 자석끼리 만나는 점을 확인할 수 있다.
            a = len(magnet[i-1])//4
            b = len(magnet[i])//4
            if magnet[i - 1][a] != magnet[i][b*3]:
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
    for i in range(M):
        result += magnet[i][0] * 2 ** i
    print('#{} {}'.format(tc, result))
