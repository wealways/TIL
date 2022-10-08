import sys
sys.stdin = open("in4-5.txt")

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr = sorted(arr,key = lambda x:x[1])

end = 0
cnt = 0
for i,a in enumerate(arr):
    if i == 0:
        cnt += 1
        end = a[1]
    else:
        if a[0] >= end:
            end = a[1]
            cnt +=1

print(cnt)

