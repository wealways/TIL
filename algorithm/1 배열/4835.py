
# 0804 - 4835
import sys
sys.stdin = open('4835.txt','r')


T = int(input())

for tc in range(1, T+1):
    length, cut = map(int, input().split())
    input_list = list(map(int, input().split()))
    M = sum(input_list[0:cut])
    m = sum(input_list[0:cut])

    for i in range(0, length-cut+1):

        test = sum(input_list[i:i+cut])
        if m >= test:
            m = test
        if M <= test:
            M = test

    print('#{} {}'.format(tc, M-m))

