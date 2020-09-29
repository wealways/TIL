import sys
sys.stdin = open('swea2819.txt','r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(dep, x, y, temp):
    temp += arr[x][y]
    if dep == 6:
        ans.append(temp)
        return
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < 4 and 0 <= newy < 4:
            dfs(dep + 1, newx, newy, temp)

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, '')
    ans = set(ans)

    print(f'#{tc} {len(ans)}')