import sys
sys.stdin = open('1209.txt', 'r')



T = 10

## 01 02 03 ... 099 // 11 12 13...199 // 00 11 22 33 .. 9999// 099 198 297

for tc in range(1,T+1):
    tc = int(input())
    input_list = [list(map(int, input().split())) for _ in range(100)]

    result_list = [0 for _ in range(202)]
    for i in range(100):
        for j in range(100):
            if i == j:
                result_list[200] += input_list[i][j]
            if i + j == 99:
                result_list[201] += input_list[i][j]

            result_list[i] += input_list[i][j]
            result_list[100+i] += input_list[j][i]

    result = 0
    for temp in result_list:
        if result <= temp:
            result = temp
    print('#{} {}'.format(tc,result))


