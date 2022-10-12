import sys
sys.stdin = open("in1.txt")

m,n = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()

lt = 0
rt = m-1

while lt<=rt:
    mid = (lt+rt)//2
    if arr[mid] == n:
        print(mid+1)
        break
    elif arr[mid]>n:
        rt = mid 
    else:
        lt = mid

