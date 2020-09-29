import sys
sys.stdin = open('swea5178.txt','r')
def postorder(node):
    if node<=N:
        postorder(node * 2)
        postorder(node * 2 + 1)
        # if node * 2 <= N:

        if node*2+1 <=N:
            tree[node] = tree[node * 2]
            tree[node] += tree[node*2+1]



T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    tree=[0]*(N+1)
    for m in range(M):
        node, data = map(int,input().split())
        tree[node]=data
    postorder(1)
    print(tree)
    print('#{} {}'.format(tc,tree[L]))

'''
교수님 풀이 1 (DFS)
for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for m in range(M):
        node, data = map(int,input().split())
        tree[node]=data
    def dfs(v):
        if v > N : return 0
        l = dfs(v*2)
        r = dfs(v*2+1)
        T[v] += l + r
        return T[v]
    dfs(1)
    print(T[L])
'''
for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for m in range(M):
        node, data = map(int,input().split())
        tree[node]=data