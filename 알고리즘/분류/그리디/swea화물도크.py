import sys
sys.stdin = open('화물도크.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int,input().split())))
    time.sort(key=lambda x:x[1])
    cnt = 1
    idx = new_idx= 0
    while new_idx <=  N-1:
        if time[idx][1]<=time[new_idx][0]:
            idx = new_idx
            cnt +=1
        else:
            new_idx += 1

    print('#{} {}'.format(tc,cnt))
