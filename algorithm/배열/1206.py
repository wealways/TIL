import sys
sys.stdin = open('1206.txt','r')


def vs(a1, a2, a3,a4,a5):
    if a3 > a2 and a3 > a1 and a3 >a4 and a3 > a5:
        return a3 - max([a1,a2,a4,a5])
    else:
        return 0


for t in range(1, 11):
    length = int(input())
    input_list = list(map(int, input().split()))
    counts = [0] * length

    for i in range(2, length - 2):
        counts[i] = vs(input_list[i-2], input_list[i - 1],input_list[i],input_list[i + 1],input_list[i+2])

    print('#{} {}'.format(t, sum(counts)))

