import sys
sys.stdin = open("in{0}.txt".format(2))

N = int(input())
visit = [0 for _ in range(N)]
def check(v):
    if v==N:
        for i in range(N):
            if visit[i]==1:
                print(i+1,end=' ')
        print()
    else:
        visit[v] = 1
        check(v+1)
        visit[v] = 0
        check(v+1)

check(0)

