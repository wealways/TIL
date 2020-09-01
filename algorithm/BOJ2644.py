
def chk(s,e):
    global cnt
    visited.append(s)
    if e in temp[s]:
        return 1
    if len(temp[s])==0 :
        return
    for i in temp[s]:
        if i not in visited:
            cnt+=1
            chk(i,e)




N = int(input())
start,end=sorted(map(int,input().split()))
start,end= 4,5
M = int(input())
temp=[[0]*(N+1) for _ in range(N+1)]
cnt = 1
visited=[]
for _ in range(M):
    i,j=map(int,input().split())
    temp[i][j],temp[j][i] = 1,1
ox= chk(start,end)

print(cnt)



