import sys

sys.stdin = open("in{0}.txt".format(2))
N = int(input())

def check(v):

    if v==1:
        print(v,end='')
        return
    else:
        check(v//2)
        print(v%2,end='')

check(N)