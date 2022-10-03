import sys
sys.stdin = open("input7.txt",'r')
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

s=e=N//2
answer = 0
for n in range(N):
    for i in range(s,e+1):
        answer += data[n][i]
    if n<N//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(answer)

# import os
# print(os.listdir())