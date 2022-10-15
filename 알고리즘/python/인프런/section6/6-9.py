import sys
import copy
sys.stdin = open("in{0}.txt".format(3))
N,F = map(int,input().split())

arr = [n+1 for n in range(N)]
visit = [0]*N
answer = []

def check(v):
    cnt = v
    temp = copy.deepcopy(visit)
    while cnt!=0:
        for i in range(cnt-1):
            temp[i]=temp[i]+temp[i+1]
        cnt-=1
    return temp[0]

def dfs(v):
    if v==N:
        if check(v)==F:
            answer.append(copy.deepcopy(visit))
    else:
        for i in range(N):
            if visit[i]==0:
                visit[i]=arr[v]
                dfs(v+1)
                visit[i]=0


dfs(0)
print(sorted(answer)[0])