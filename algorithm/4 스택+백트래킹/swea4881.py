# def per(k):
#     if k==N:
#         print(s)
#
#     else:
#         for i in range(N):
#             if not visited[i]:
#                 s[k]=i
#                 visited[i]=True
#                 per(k+1)
#                 visited[i]=False
#
#
#
# s=[0,0,0]
# lst=[1,5,10]
# N=len(s)
# visited=[False]*N
# per(0)
#
import sys
sys.stdin = open('swea4881.txt','r')
T = int(input())

def chk(y):
    global temp,result
    if result < temp:
        return
    if y == N:
        if result >= temp:
            result = temp
        return
    else:
        for x in range(N):
            if not visited[x]:
                visited[x]=True
                temp += input_list[y][x]
                chk(y+1)
                visited[x] = False
                temp -= input_list[y][x]

for tc in range(1,T+1):
    N = int(input())
    input_list = [list(map(int,input().split())) for _ in range(N)]
    visited=[0]*N
    temp,result = 0,9999999
    chk(0)
    print(f'#{tc} {result}')