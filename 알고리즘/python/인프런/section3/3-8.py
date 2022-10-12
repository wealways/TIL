import sys

sys.stdin = open("input8.txt")

n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]

for i in range(int(input())):
    x,t,y = map(int,input().split())

    if t ==0:
        data[x-1] = data[x-1][y:]+data[x-1][:y]
    else:
        data[x-1] = data[x-1][n-y:]+data[x-1][:n-y]

print(data)
answer = 0
s=0
e=n
for i in range(n):
    for j in range(s,e):
        answer += data[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(answer)