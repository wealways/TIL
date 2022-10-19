import sys
sys.stdin = open("in{}.txt".format(5))
N = int(input())

arr = list(map(int,input().split()))

maxV = sum(arr)
temp = []
def dfs(v,total):
    if v == N:
        if total in range(1,maxV):
            temp.append(total)
        return
    else:
        dfs(v+1,total+arr[v])
        dfs(v+1,total-arr[v])
        dfs(v+1,total)

dfs(0,0)
temp = set(temp)
print(maxV-len(temp)-1)