import sys
sys.stdin = open("input9.txt")
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

def check(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        tempx =x+ dx[i]
        tempy =y+ dy[i]
        if tempx>=0 and tempx<n and tempy>=0 and tempy<n and data[x][y]<=data[tempx][tempy]:
            return False
    return True

answer = 0
for x in range(n):
    for y in range(n):
        if check(x,y):
            answer +=1
print(answer)
