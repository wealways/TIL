import sys
sys.stdin = open('swea5102.txt','r')

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    G = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int,input().split())
        G[u][v] = G[v][u] = 1
    s, e = map(int,input().split())
    visit = [0]*(V+1)
    Q=[s]
    visit[s] = 1
    while Q :
        v = Q.pop(0)
        for w in range(1,V+1):
            if v==e:
                break
            if G[v][w] and visit[w]==0:
                visit[w]=visit[v]+1
                Q.append(w)

    print(visit[e]-1)