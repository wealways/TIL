import sys
sys.stdin = open("in{0}.txt".format(5))

N = int(input())
arr = list(map(int,input().split()))
M = int(input())

minV = 9999999999
def check(v,sumV):
    global minV

    if minV <v:
        return
    if sumV > M:
        return
    if sumV == M:
        minV = min(v,minV)
        return
    else:
        for i in range(N):
            check(v+1,sumV+arr[i])
arr.sort(reverse=True)
check(0,0)
print(minV)