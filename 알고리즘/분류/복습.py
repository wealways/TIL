import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N-1):
    x,y = map(int,input().split())
    arr[x][y] = 1
    # arr[y][x] = 1

visit = [0]*(N+1)

def dfs(v,stop,answer):
    if v==stop:
        return 1
    else:
        for i in range(1,N+1):
            if visit[i] == 0 and arr[v][i]==1:
                visit[i] = 1
                print(i,v)
                dfs(i,stop,v)
                visit[i] = 0
                
for i in range(2,N+1):
    visit[i] = 1
    result = dfs(1,i,0)
    visit[i] = 0
    print(result)
    print('====')

