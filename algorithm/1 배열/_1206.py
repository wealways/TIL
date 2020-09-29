#교수님 코드

t=10
def getmax(i):
    ...


for tc in range(1,t+1):
    N = int(input())
    BRD = list(map(int,input().split()))
    result = 0
    for i in range(2,N-2):
        maxV = getmax(i)#왼쪽 2개 오른쪽 2개 중 제일 큰 값
        if maxV < BRD[i]:
            cnt = BRD[i] - maxV

        result += cnt

    print(result)