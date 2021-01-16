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
            if D[i]> G[curV][i]:
                D[i] = G[curV][i]
    return D

T = int(input())
for tc in range(1, 1 + T):
    V, E = map(int, input().split())
    G = [[float('inf')]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2]=w
        G[n2][n1]=w
    # pprint(G)
    # print(mst_prim())
    print('#{} {}'.format(tc, sum(mst_prim()[1:])))
