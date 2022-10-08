import sys
sys.stdin = open("in4-7.txt")
l = int(input())
arr = list(map(int,input().split()))
m = int(input())

while m>0:
    
    maxT = max(arr)
    maxIdx = arr.index(maxT)
    arr[maxIdx] -= 1
    minT = min(arr)
    minIdx = arr.index(minT)
    arr[minIdx] += 1
    m -= 1

print(max(arr)-min(arr))