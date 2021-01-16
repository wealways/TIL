# import sys
# sys.stdin = open('swea10888.txt','r')
#
# from itertools import combinations
#
# T = int(input())
# T=1
# for tc in range(1,T+1):
#     N = int(input())
#     food_map = [list(map(int,input().split())) for _ in range(N)]
#
#     # 순회하며 음식점 좌표 찾아 리스트 만들기
#     restruant = []
#     for i in range(N):
#         for j in range(N):
#             if food_map[i][j]>1:
#                 restruant.append((i,j))
#     print(restruant)
#     minV = N*N
#     print(list(combinations(restruant, 1))[0])
#     # for n in range(1,len(restruant)):
#     #     combi = list(combinations(restruant, n))
#     #     for c in combi:
#     #
