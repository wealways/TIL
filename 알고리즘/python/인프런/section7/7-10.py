import sys
sys.stdin = open("in{}.txt".format(1))

arr = [list(map(int,input().split())) for _ in range(7)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
def dfs(x,y):
    global cnt
    if x==6 and y==6:
        cnt += 1
        return
    else:
        for i in range(4):
            tempx = x+dx[i]
            tempy = y+dy[i]
            if 0<=tempx<7 and 0<=tempy<7 and arr[tempx][tempy] == 0:
                arr[tempx][tempy] = 1
                dfs(tempx,tempy)
                arr[tempx][tempy] = 0

arr[0][0]=1
dfs(0,0)
print(cnt)