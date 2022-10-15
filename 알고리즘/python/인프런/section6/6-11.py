import sys
from copy import deepcopy
sys.stdin = open("in{0}.txt".format(1))

N,K = map(int,input().split())
arr = list(map(int,input().split()))
M = int(input())

temp = [0]*K
answer = []
def dfs(v,s,sumV):
    if v==K:
        if sumV%M == 0:
            answer.append(deepcopy(temp))
        return
    else:
        for i in range(s,N):
            temp[v] = i
            dfs(v+1,i+1,sumV+arr[i])

dfs(0,0,0)
print(len(answer))
