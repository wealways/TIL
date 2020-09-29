import sys
sys.stdin = open('1258.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dic = {}
    for y in range(N):
        cnt = 0
        for x in range(N):
            if arr[y][x] > 0:
                cnt += 1

            elif arr[y][x] == 0 and cnt!=0:
                dic[cnt] = dic.get(cnt,0)+1
                cnt = 0
        if cnt>0:
            dic[cnt] = dic.get(cnt,0)+1

    result = []

    for x,y in dic.items():
        result.append((x*y,y,x))
    result.sort()
    print('#{} {} '.format(tc, len(result)), end='')
    for i in range(len(result)):
        print(result[i][1],result[i][2], end=' ')
    print()

