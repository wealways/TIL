import sys
sys.stdin = open("in4-10.txt")

n = int(input())

arr = list(map(int,input().split()))

temp = [0 for _ in range(n)]

print(temp)
for i in range(n):

    cnt = 0
    for j in range(n):
        if arr[i] == cnt and temp[j] == 0:
            temp[j] = i+1
            break
        elif temp[j] == 0:
            cnt += 1

print(temp)