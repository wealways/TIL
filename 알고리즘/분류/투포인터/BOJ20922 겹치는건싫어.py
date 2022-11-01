import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))

cnt = [0]*(max(arr)+1)
lt = rt = 0
answer =0
while rt<N:
    if cnt[arr[rt]]<K:
        cnt[arr[rt]] += 1
        rt += 1
    else:
        cnt[arr[lt]] -= 1
        lt += 1
    answer = max(answer,rt-lt)
print(answer)