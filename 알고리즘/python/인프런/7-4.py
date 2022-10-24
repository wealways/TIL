import sys
from copy import deepcopy
sys.stdin = open("in{}.txt".format(5))

T = int(input())
coins = []
K = int(input())
for _ in range(K):
    coins.append(list(map(int,input().split())))

temp = [0]*K
answer = []
def dfs(v,sumV):
    if sumV >T:
        return
    if v==K:
        if sumV == T:
            answer.append(deepcopy(temp))
        return
    else:
        for i in range(coins[v][1]+1):
            temp[v] = i
            dfs(v+1,sumV+coins[v][0]*i)
            temp[v] = 0
dfs(0,0)
print(answer)
print(len(answer))