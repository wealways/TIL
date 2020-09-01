def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = [0] * 5
for i in range(5):
    arr[i] = list(map(int, input().split()))

total = 0
for i in range(5):
    for j in range(5):