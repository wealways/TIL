import sys
from copy import deepcopy
sys.stdin = open("in{0}.txt".format(1))

N,M = map(int,input().split())

temp = [0]*M
cnt = 0
def check(v):
    global cnt
    if v == M:
        for m in range(M):
            print(temp[m],end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(N):
            temp[v] = i+1
            check(v+1)
            
        


check(0)
print(cnt)