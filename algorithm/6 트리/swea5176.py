import sys
sys.stdin = open('swea5176.txt','r')

def bst(node):
    global data
    if node<=N:
        bst(node*2)
        tree[node]=data
        data+=1
        bst(node*2+1)

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    data = 1
    bst(1)
    print(tree)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))

'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0]*(N+1)
    cnt=0
    def inorder(v):
        global cnt
        if v>N : return
        inorder(v*2)
        T[v] = cnt
        cnt+1
        inorder(v*2+1)
    inorder(1)
        
'''

