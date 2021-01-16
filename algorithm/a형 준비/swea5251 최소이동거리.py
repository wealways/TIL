import sys
sys.stdin = open('input1.txt')
def mst_prim():
    curV=0
    D = [float('inf')]*(V+1)
    u=[0]
    for i in range(V+1):
        D[i]=G[0][i]
    while len(u) <=V :
        minV=float('inf')
        for i in range(V+1):
            if i in u:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        u.append(curV)

        for i in range(V+1):
            if i in u:
                continue
            if D[i]>D[curV]+ G[curV][i]:
                D[i] = D[curV]+G[curV][i]
        if curV == V:
            return D

def dijstra():
    dist = [float('inf')] *(V+1)
    visited = [0]*(V+1)
    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = float('inf')

        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx=i
                min_value=dist[i]
        visited[min_idx]=1

        for j in range(V+1):
            if not visited[j] and dist[j] > dist[min_idx]+G[min_idx][j]:
                dist[j] = dist[min_idx]+G[min_idx][j]

    return dist[V]

import heapq
def dijstra_heap():
    dist = [float('inf')]*(V+1)
    visited = [0]*(V+1)

    heap=[]
    dist[0]=0
    # 가중치와 정점
    heapq.heappush(heap,(0,0))
    while heap:
        w,v = heap.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v]=w

            for i in range(v+1):
                if not visited[i] and  dist[i] > dist[v]+G[v][i]:
                    heapq.heappush(heap,(dist[v]+G[v][i], i))
        return dist[V]


T = int(input())
for tc in range(1, 1 + T):
    V, E = map(int, input().split())
    G = [[float('inf')]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2]=w

    print('#{} {}'.format(tc, mst_prim()[V]))
    print('#{} {}'.format(tc,dijstra()))
    print('#{} {}'.format(tc, dijstra_heap()))
    print()