import sys
sys.stdin = open("in4-3.txt")

n,m = map(int,input().split())
arr = list(map(int,input().split()))

lt = min(arr)
rt = sum(arr)
maxV = max(arr)

def check(mid):
    cnt = 1
    sumV = 0
    for a in arr:
        if sumV + a >mid:
            cnt += 1
            sumV = a
        else:
            sumV += a
    
    return cnt


answer = 0
while lt <= rt:
    mid =(lt+rt)//2
    if mid>=maxV and check(mid)<=m:
        answer = mid
        rt = mid-1
    else:
        lt = mid +1
print(answer)


    