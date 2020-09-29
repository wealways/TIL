import sys
sys.stdin = open('4839.txt')


def binary_search(P,ans):
    start = 1
    cnt = 1
    end = P
    while True:
        cur = (start + end) //2

        if cur == ans:
            return cnt
        elif cur > ans:
            end = cur

        else:
            start = cur
        cnt += 1



T = int(input())

for tc in range(1,T+1):
    P, Pa,Pb = map(int,input().split())
    a = binary_search(P,Pa)
    b = binary_search(P,Pb)
    result = ''
    if a>b:
        result = 'B'
    elif a<b:
        result = 'A'
    else:
        result = 0
    print('#{} {}'.format(tc,result))