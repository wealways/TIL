
import sys
sys.stdin = open('4843.txt','r')

T = int(input())

for tc in range(1,T+1):

    N = int(input())
    input_list = list( map(int,input().split()))

    # pop(max) pop(min) pop(max) ....
    #
    chk = len(input_list)
    temp = []
    while chk > 0:

        temp.append(max(input_list))
        input_list.remove(max(input_list))
        chk -= 1
        if chk == 0:
            break;
        temp.append(min(input_list))
        input_list.remove(min(input_list))
        chk -= 1
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(temp[i], end=' ')
    print()