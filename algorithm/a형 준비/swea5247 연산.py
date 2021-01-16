from collections import deque

def chk(v):
    Q = deque()
    visit= [0]*1000001
    Q.append((v,0))
    visit[v]=1
    while Q:
        # v,cnt = Q.pop(0)
        v,cnt = Q.popleft()
        if v==M:
            break
        else:
            t= [v*2,v+1,v-1,v-10]
            for i in range(4):
                if t[i]>0 and t[i]<=1000000 and not visit[t[i]]:
                    Q.append((t[i],cnt+1))
                    visit[t[i]]=1
    return cnt

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    print('#{} {}'.format(tc,chk(N)))