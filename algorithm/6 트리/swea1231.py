import sys
sys.stdin = open('swea1231.txt','r')

def inorder(T):
    if T:
        inorder(tree[T][1])
        print(f'{tree[T][0]}',end='')
        inorder(tree[T][2])

for tc in range(1,11):
    N = int(input())
    tree=[[0]*3 for _ in range(N+1)]
    for _ in range(N):
        temp = list(input().split())
        parent = int(temp[0])
        tree[parent][0] = temp[1]
        if len(temp)>=3:
            for i in temp[2:]:
                child=int(i)
                if not tree[parent][1]:
                    tree[parent][1] = child
                else:
                    tree[parent][2] = child
    print(f'#{tc}',end=' ')
    inorder(1)
    print()