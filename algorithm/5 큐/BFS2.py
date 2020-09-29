'''
인접 리스트 이용하기
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
import sys
sys.stdin = open('BFS1.txt','r')
def bfs(v):
   Q = []
   visit = [0]*(V+1)

   #endQ
   Q.append(v)
   visit[v]=1
   print(v,end=' ')
   while Q:
       v = Q.pop(0)
       for w in G[v]:
           if not visit[w]:
                Q.append(w)
                visit[w]=1
                print(w,end=' ')

# 인접리스트
V,E = map(int,input().split())
temp = list(map(int,input().split()))
G = [[] for _ in range(V+1)]

# 인접리스트 저장
for i in range(E):
    s,e = temp[2*i],temp[2*i+1]
    G[s].append(e)
    G[e].append(s)

#인접행렬 출력
for i in range(1,V+1):
    print('{} {}'.format(i,G[i]))

bfs(1)

#