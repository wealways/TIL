import sys
sys.stdin= open("in{0}.txt".format(3))

C,N = map(int,input().split())

dogs = [int(input()) for _ in range(N)]
maxV = 0
def check(v,kg):
    global maxV

    if kg > C:
        return
    
    if v == N:
        maxV = max(maxV,kg)
    else:
        check(v+1,kg)
        check(v+1,kg+dogs[v])

check(0,0)
print(maxV)


