import sys
sys.stdin = open("in{}.txt".format(3))

N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

visit = [0]*N
maxV = 0
def dfs(v,sumV,timeV):
    global maxV
    if timeV >M:
        return
    if v==N:
        maxV = max(sumV,maxV)
        return
    else:
        if visit[v]==0:
            visit[v]=1
            dfs(v+1,sumV+arr[v][0],timeV+arr[v][1])
            visit[v]=0
            dfs(v+1,sumV,timeV)

dfs(0,0,0)

print(maxV)