import sys
sys.stdin = open("in{0}.txt".format(1))

N,M = map(int,input().split())

visit = [0]*N
cnt = 0
def dfs(v,s):
    global cnt
    if v == M:
        for i in range(M):
            print(visit[i],end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(s,N):
            visit[v] = i+1
            dfs(v+1,i+1)

dfs(0,0)
print(cnt)