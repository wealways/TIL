import sys
sys.stdin = open('4831.txt', 'r')


T = int(input())

for tc in range(1,T+1):

    K, N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    result_list = [0] * N
    for i in input_list:
        result_list[i] = 1

    idx = 0
    result = 0

    while idx < N -K :
        temp = result_list[idx+1:idx+K+1]

        if sum(temp):
            plus_idx = 0
            for n,i in enumerate(temp):
                if i==1:
                    plus_idx = n+1
                    continue

            idx += plus_idx
            result += 1

        else:
            result = 0
            break;


    print('#{} {}'.format(tc,result))
