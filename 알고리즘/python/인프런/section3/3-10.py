import sys
sys.stdin = open("input10.txt")

data = [list(map(int,input().split())) for _ in range(9)]


def check(x,y):
    temp = [0 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            temp[data[x+i][y+j]-1] = 1
    
    if sum(temp) == 9:
        return True
    else:
        return False



answer = 'YES'
for i in range(9):

    tempX = [0 for _ in range(9)]
    tempY = [0 for _ in range(9)]
    for j in range(9):

        # 가로줄
        tempX[data[i][j]-1] = 1
        # 세로줄
        tempY[data[j][i]-1] = 1
        # 정사각형
        if i in [0,3,6] and j in [0,3,6]:
            if check(i,j) == False:
                answer = 'NO'
    
    if sum(tempX) !=9 or sum(tempY) !=9:
        answer = 'NO'
print(answer)