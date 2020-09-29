import sys
sys.stdin = open('swea5174.txt','r')

def preorder(T):
    global cnt

    if T:
        cnt+=1
        preorder(tree[T][0])
        preorder(tree[T][1])

T= int(input())

for tc in range(1, T+1):
    E,N = map(int, input().split())
    input_list = list(map(int, input().split()))
    tree = [[0]*2 for _ in range(E+2)]
    for i in range(len(input_list)//2):
        parent,child = input_list[i*2],input_list[i*2+1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    cnt=0
    preorder(N)
    print(f'#{tc} {cnt}')


'''
# 교수님 풀이 1 (DFS)
T= int(input())

for tc in range(1, T+1):
    E,N = map(int, input().split())
    # 노드번호 1~E+1
    L = [0] * (E+2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    arr = list(map(int, input().split()))
    for i in range(0,E*2,2)
        p,c = arr[i],arr[i+1]

        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p
    
    def traverse(v):
        
        if v == 0: return 0
        
        l = traverse(L[v])
        r = traverse[R[v]]
        return l + r + 1
    print(traverse(N))
'''
'''
# 교수님 풀이 2 (BFS)
T= int(input())

for tc in range(1, T+1):
    E,N = map(int, input().split())
    # 노드번호 1~E+1
    L = [0] * (E+2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    arr = list(map(int, input().split()))
    for i in range(0,E*2,2)
        p,c = arr[i],arr[i+1]

        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p

    ans = 0
    Q = [N]
    while Q:
        v = Q.pop(0)
        if v == 0: continue
        ans += 1
        Q.append(L[v])
        Q.append(R[v])
    print(ans)
'''