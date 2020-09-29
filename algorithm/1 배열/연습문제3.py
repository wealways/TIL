## 달팽이 정렬

#def
def getMin(curV):
    minV = 1000000000000
    for i in range(5):
        for j in range(5):
            if minV > src[i][j] and src[i][j] > curV:
                minV = src[i][j]
    #src에서 curV보다 큰 값 중에 가장 작은 값을 구해서 리턴



def iswall(X,Y):
    '''
    진짜,
    이미 dst[Y][X] 값이 있는 경우에도 벽으로 생각해야해
    '''
    if X <0 or X>=5:
        return True
    if Y < 0 or Y > 5:
        return True
    if dst[y][x] != 0:
        return True
    return False

# src에 입력

# dst 배열은 0으로 초기화
dst = [[0]*5 for _ in range(5)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dir = 0

curX = curY = 0
curV = 0
for i in range(25):
    val = getMin(curV)
    dst[curY][curX] = val
    curV = dst[curY][curX]
    testX = curX + dx[dir]
    testY = curY + dy[dir]
    if iswall(testX, testY):
        dir = (dir+1)%4
    curX = curX + dx[dir]
    curY = curY + dy[dir]
