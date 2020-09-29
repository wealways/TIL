import sys
sys.stdin = open('4869.txt','r')

def find(N):
    n = N//10
    if n>=2 and n>=len(memo):
        memo.append(find(10*(n - 1)) + 2*find(10*(n - 2)))
    return memo[n]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    memo = [0,1,3]
    print(find(N))