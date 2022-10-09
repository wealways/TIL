import sys
sys.stdin = open("in4-8.txt")

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)


visited = [0 for _ in range(n)]

answer = 0
while sum(visited) != n:
    temp = 0
    answer += 1
    for i,a in enumerate(arr):
        if visited[i]!=1 and temp + a <=m:
            temp += a
            visited[i] = 1

print(answer)