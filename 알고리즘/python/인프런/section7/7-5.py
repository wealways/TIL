import sys

sys.stdin = open("in{}.txt".format(5))

N = int(input())
coins = [int(input()) for _ in range(N)]
visit = [0]*N

answer = 999999
def dfs(v):
    global answer
    if v== N:
        if 0 in visit and 1 in visit and 2 in visit:
            a = b = c = 0
            for idx,data in enumerate(visit):
                if data==0:
                    a += coins[idx]
                elif data==1:
                    b += coins[idx]
                else:
                    c += coins[idx]
            if len(set([a,b,c]))==3:
                temp =max([a,b,c]) - min([a,b,c])
                answer = min(answer,temp)

                return
    else:
        for i in range(3):
            visit[v] = i
            dfs(v+1)
            visit[v] = 0

dfs(0)
print(answer)