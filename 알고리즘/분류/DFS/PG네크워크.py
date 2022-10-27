n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# return 2

visit = [0]*n
answer = 0

def dfs(v):
    visit[v] = 1
    for i in range(n):
        if v!=i and visit[i]==0 and computers[v][i]==1:
            dfs(i)
for i in range(n):
    if visit[i]==0:
        dfs(i)
        answer += 1
print(answer)