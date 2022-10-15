import sys
sys.stdin = open("in{0}.txt".format(1))

N,M = map(int,input().split())

visit = [0]*N
answer = [0]*N
cnt = 0
def check(v):
    global cnt
    if v == M:
        for i in range(N):
            if answer[i] != 0:
                print(answer[i],end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(N):
            if visit[i]==0:
                visit[i]=1
                answer[v]=i+1
                check(v+1)
                visit[i]=0
            

check(0)
print(cnt)