N,E =7,8
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

def dfs(v):
    visited[v]=1
    print(v,end=' ')
    for w in range(1,N+1):
        if visited[w]==0 and G[v][w]==1:
            dfs(w)

G = [[0]*(N+1) for _ in range(N+1)]
visited= [0]*(N+1)

for i in range(E):
    s,e = temp[2*i],temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1



dfs(1)















#
#
#
# def dfs(v):
#     visited[v]=1
#     print(v, end=' ')
#     for w in range(1,N+1):
#         if visited[w]==0 and G[v][w]==1:
#             dfs(w)
#
# visited = [0]*(N+1)
# G = [[0]*(N+1) for _ in range(N+1)]
#
#
# for i in range(E):
#     s = temp[2*i]
#     e = temp[2*i+1]
#     G[s][e] = 1
#     G[e][s] = 1
#
# dfs(1)