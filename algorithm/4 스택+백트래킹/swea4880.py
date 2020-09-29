import sys
sys.stdin = open('swea4880.txt','r')
# 1 가위 2 바위 3 보
def win(x,y):
    if (x == 1 and y == 3) or (x == 1 and y == 1):
        return 1
    elif (x == 2 and y == 1) or (x == 2 and y == 2):
        return 1
    elif (x == 3 and y == 2) or (x == 3 and y == 3):
        return 1
    return 0

def chk(arr):
    if len(arr) < 2:
        return arr[0]
    n=len(arr)
    if n %2 ==0 :
        left = arr[:n//2]
        right = arr[n//2:]
    else:
        left = arr[:n // 2 +1]
        right = arr[n // 2 +1:]
    x = chk(left)
    y = chk(right)
    if win(x[0],y[0]): return x
    else: return y


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    input_list = list(map(int,input().split()))
    input_list = [(n, i+1) for i, n in enumerate(input_list)]
    print(f'#{tc} {chk(input_list)[1]}')
