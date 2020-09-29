import sys
sys.stdin = open('swea5099.txt','r')

T= int(input())
# for tc in range(1,T+1):
#     # N 화덕크기,M 피자수
#     N,M = map(int,input().split())
#     pizza = [0] + list(map(int,input().split()))
#
#     #피자번호
#     oven = [i for i in range(1,N+1)]
#
#     # 추가할 피자 번호
#     pos = N+1
#     while len(oven)>1:
#         num = oven.pop(0)
#         pizza[num] = pizza[num]//2
#         if pizza[num]:
#             oven.append(num)
#         else:
#             if pos<=M:
#                 oven.append(pos)
#                 pos += 1
#     print(oven[0])

# 편할 수도 있는 방법
for tc in range(1,T+1):
    # N 화덕크기,M 피자수
    N,M = map(int,input().split())
    pizza = [0] + list(map(int,input().split()))

    #피자번호
    oven = [[i,pizza[i]] for i in range(1,N+1)]
    remain = [[i,pizza[i]] for i in range(N+1,M)]
    # 추가할 피자 번호

    pos = N+1
    while len(oven)>1:
        num,cheeze = oven.pop(0)
        cheeze = cheeze//2
        if cheeze:
            oven.append([num,cheeze])
        else:
            if remain:
                oven.append(remain.pop(0))

    print(oven[0][0])
