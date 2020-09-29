import sys
sys.stdin = open('4864.txt','r')

def brute(p,t):
    i,j = 0,0
    while i < len(p) and j <len(t):
        if p[i] != t[j]:
            j -=i
            i =-1
        j +=1
        i += 1
    if i ==len(p):
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    pattern = list(input())
    text = list(input())
    print('#{} {}'.format(tc,brute(pattern,text)))
