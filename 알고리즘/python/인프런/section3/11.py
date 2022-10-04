import sys
sys.stdin = open('input11.txt')

data = [list(map(int,input().split())) for _ in range(7)]

answer = 0
for i in range(7):
    for j in range(3):
        tempX = []
        for k in range(j,j+5):
            tempX.append(data[i][k])
        if tempX == tempX[::-1]:
            answer += 1
        tempY = []
        for k in range(j,j+5):
            tempY.append(data[k][i])
        if tempY == tempY[::-1]:
            answer += 1
print(answer)