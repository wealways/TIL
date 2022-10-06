import sys
sys.stdin = open("in4-2.txt")

n, k = map(int,input().split())

arr = [int(input()) for _ in range(n)]

lt = 1
rt = max(arr)

def check(mid):
    temp = 0
    for a in arr:
        temp += a//mid
    
    if temp>=k:
        return True
    else:
        return False

answer = 0
while lt<=rt:
    mid = (lt+rt)//2
    if check(mid):
        answer = mid
        lt = mid +1
    else:
        rt = mid -1
print(answer)