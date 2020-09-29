import sys
sys.stdin = open('tree.txt','r')
def preorder(T):
    if T:
        print('%d' % T, end=' ')
        preorder(tree[T][0])
        preorder(tree[T][1])

n = int(input())
tree=[[0]*2 for _ in range(n+1)]
templ = list(map(int,input().split()))
for i in range(len(templ)//2):
    parent, child = templ[i*2] , templ[i*2+1]
    if not tree[parent][0]:
        tree[parent][0]=child
    else:
        tree[parent][1] = child

preorder(1)