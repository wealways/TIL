import sys
sys.stdin = open('in4-4.txt')

n,c = map(int,input().split())

house = [int(input()) for _ in range(n)]

house.sort()


def check(mid):
    temp = 0
    cnt = 0
    for i in range(n):
        if i ==0:
            temp = house[0]
            cnt +=1
        else:
            if house[i]-temp >= mid:
                temp = house[i]
                cnt+=1
    
    if cnt == c:
        return True
    else:
        return False




lt = house[1]-house[0]
rt = house[n-1]-house[0]

answer = 0
while lt<=rt:
    mid  = (lt+rt)//2
    if check(mid):
        answer = mid
        lt = mid+1
    else:
        rt = mid-1

print(answer)