import sys
sys.stdin = open('4834.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    case =int(input())
    input_list = [int(n) for n in input()]

    result_list = [0]*10
    for num in input_list:
        result_list[num] += 1
    result = 0
    result_idx = 0
    for i, n in enumerate(result_list):
        if result <= n:
            result = n
            result_idx = i
    print('#{} {} {}'.format(tc,result_idx, result))
