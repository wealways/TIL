import sys
sys.stdin = open("in4-6.txt")

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

print(arr)
arr = sorted(arr,key=lambda x:(-x[1],-x[0]))


cnt = 0
temp = [0,0]
for a in arr:
    if temp[0]<= a[0] or temp[1]<=a[1]:
        temp = a
        cnt += 1

print(cnt)