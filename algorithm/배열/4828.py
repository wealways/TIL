import sys

sys.stdin = open('4828.txt','r')

T = int(input())

for tc in range(1,T+1):
    num = int(input())
    input_list = list(map(int,input().split()))

    M = input_list[0]
    m = input_list[0]

    for n in input_list:
        if M <= n:
            M = n
        if m >= n:
            m = n
    print('#{} {}'.format(tc,M-m))