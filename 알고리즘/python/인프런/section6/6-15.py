import sys
sys.stdin = open("in{0}.txt".format(1))

N,M = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
# visit = [[0]*(N+1) for _ in range(N+1)]


for _ in range(M):
    x,y = map(int,input().split())
    arr[x][y] = 1
# print(arr)
cnt = 0
# path= []
def dfs(v):
    global cnt
    if v == N:
        # print(path)
        cnt += 1
        return
    else:
        for i in range(1,N+1):
            if arr[v][i] == 1 and visit[v]==0:
                visit[v] = 1
                # path.append(i)
                dfs(i)
                # path.pop()
                visit[v] = 0

dfs(1)
print(cnt)