import sys
sys.stdin = open('tree.txt','r')

def preorder(node):
    global cnt
    if node:
        print(node,end= ' ')
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

# 정점과 간선
V = int(input())
E = V-1
# 왼쪽,오른쪽,부모 3열
tree = [[0]*3 for _ in range(V+1)]
temp = list(map(int,input().split()))
cnt = 0
for i in range(E):
    parent,child = temp[i*2],temp[i*2+1]
    if tree[parent][0]==0:
        tree[parent][0]=child
    else:
        tree[parent][1]=child
    tree[child][2]=parent
preorder(1)