import sys
sys.stdin = open('1221.txt','r')

T = int(input())

new = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1,T+1):
    t, N = input().split()
    t = int(t[1:])
    N = int(N)
    temp = []
    result = []
    input_list = input().split()

    for i in input_list:
        temp.append(new.index(i))
    temp.sort()

    for i in temp:
        result.append(new[i])
    print('#{}'.format(t))
    print(' '.join(result))