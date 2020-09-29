import sys
sys.stdin = open('4837.txt')

def bit(N,ans):
    cnt = 0
    arr = [n for n in range(1,13)]
    for i in range(1<<12):
        temp = []
        for j in range(12):

            if i & (1<<j):
                temp.append(arr[j])


        if sum(temp) == ans and len(temp)==N:
            cnt +=1

    return cnt

T = int(input())

for tc in range(1,T+1):
    N,ans = map(int,input().split())

    print('#{} {}'.format(tc, bit(N,ans)))