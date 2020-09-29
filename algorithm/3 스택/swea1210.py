import sys
sys.stdin = open('swea1210.txt','r')

def chk(y,x):
    visited.append((y,x))

    if y==0:
        result.append(x)
        return

    for i in range(3):
        newy = y + dy[i]
        newx = x + dx[i]
        if 0<= newy <=99 and 0<=newx<= 99:
            if input_list[newy][newx] == 1 and (newy,newx) not in visited:
                chk(newy,newx)


for tc in range(1, 11):
    tc = int(input())
    input_list = [list(map(int, input().split())) for _ in range(100)]

    start_y = 99
    start_x = input_list[99].index(2)

    dy = [0, 0, -1]
    dx = [-1, 1, 0]
    result = []
    visited = []
    chk(start_y, start_x)
    print(f'#{tc} {result[0]}')