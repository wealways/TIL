import sys
from collections import deque

sys.stdin = open("in{}.txt".format(5))
S,E = map(int,input().split())

maxV = 10000
visit = [-1]*(maxV+1)
q = deque()

q.append(S)
visit[S] = 0

while q:
    now = q.popleft()
    if now == E:
        break
    for next in [now-1,now+1,now+5]:
        if 0<next<=maxV:
            if visit[next] == -1:
                q.append(next)
                visit[next] = visit[now] +1

print(visit[E])
