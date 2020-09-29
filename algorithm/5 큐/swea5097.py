import sys
sys.stdin = open('swea5097.txt','r')

T= int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     input_list = list(map(int,input().split()))
#
#     for _ in range(M%N):
#         input_list.append(input_list.pop(0))
#     print(f'#{tc} {input_list[0]}')

# # 선형큐 사용법
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     Q = list(map(int,input().split())) +([0]*M)
#     f,r = -1,N-1
#
#     for _ in range(M):
#         f+=1
#         r+=1
#         Q[r]=Q[f]
#     print(Q[f+1])

# 원형큐 사용법
for tc in range(1,T+1):
    N,M = map(int,input().split())
    Q = [0]+list(map(int,input().split()))
    f,r = 0,N
    size = N+1

    for _ in range(M):
        f = (f+1) % size
        r = (r+1) % size
        Q[r]=Q[f]

    print(Q[(f+1)%size])