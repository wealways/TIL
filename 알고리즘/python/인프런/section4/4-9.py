import sys
sys.stdin = open("in4-9.txt")

n = int(input())
arr = list(map(int,input().split()))

lt = 0
rt = n-1
answer = ''
temp = []
maxV = 0
while lt<=rt:

    if maxV < arr[lt]:
        temp.append([arr[lt],'L'])
    if maxV < arr[rt]:
        temp.append([arr[rt],'R'])
    temp.sort()

    if len(temp) == 0:
        break
    else:
        answer += temp[0][1]
        maxV = temp[0][0]
        if temp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    temp = []

print(len(answer))
print(answer)