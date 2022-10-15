import sys
sys.stdin = open("in{0}.txt".format(1))

N = int(input())

arr = list(map(int,input().split()))

def check(v,sumV):
    if  sumV > sum(arr)/2:
        return
    
    if v == N:
        if sumV == sum(arr)/2:
            print('YES')
            sys.exit(0)
    else:
        check(v+1,sumV+arr[v])
        check(v+1,sumV)

check(0,0)
print('NO')