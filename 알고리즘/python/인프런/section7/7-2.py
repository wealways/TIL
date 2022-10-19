import sys
sys.stdin = open("in{}.txt".format(2))

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
maxV = 0

visit = [0]*N

def dfs(v,sumV):
    global maxV
    if v>=N-1:
        maxV = max(maxV,sumV)
        return
    else:
        dfs(v+arr[v][0],sumV+arr[v][1])
        dfs(v+1,sumV)

dfs(0,0)
print(maxV)

