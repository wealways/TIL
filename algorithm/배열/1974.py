import sys
sys.stdin = open('1974.txt','r')


def chk0(arr):
    for i in range(1,10):
        if arr[i-1] != i:
            return 0
    return 1


def chk1(arr,x,y):
    temp = []
    for i in range(x,x+3):
        for j in range(y,y+3):
            temp.append(arr[i][j])
    temp.sort()
    return chk0(temp)


T = int(input())

for tc in range(1,T+1):
    input_list = [list(map(int,input().split())) for _ in range(9)]
    x = y = [0,3,6]
    result = 1

    for i in x:
        for j in y:
            result *= chk1(input_list, i, j)


    for i in range(9):
        temp_1 = []
        temp_2 = []
        for j in range(9):
            temp_1.append(input_list[i][j])
            temp_2.append(input_list[j][i])
        temp_1.sort()
        result *= chk0(temp_1)
        temp_2.sort()
        result *= chk0(temp_2)

    print('#{} {}'.format(tc, result))