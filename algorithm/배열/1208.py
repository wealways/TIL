import sys
sys.stdin = open('1208.txt','r')
T = 10

for tc in range(1,T+1):
    dump_num = int(input())
    input_list = list(map(int,input().split()))

    length = len( input_list )

    while dump_num>0:

        M = max(input_list)
        m = min(input_list)
        if M - m != 0:
            input_list[input_list.index(M)] -= 1
            input_list[input_list.index(m)] += 1
            dump_num -= 1
        else:
            break;


    print('#{} {}'.format(tc,max(input_list) - min(input_list)))