import sys
sys.stdin = open('swea4047.txt','r')

T = int(input())
for tc in range(1,T+1):
    input_list = input()
    temp= []
    chk = {
        'S':13,
        'D':13,
        'H':13,
        'C':13
    }
    ans=''
    for i in range(len(input_list)//3):
        temp.append(input_list[i*3:i*3+3])

    if len(temp) != len(set(temp)):
        ans='ERROR'
    else:
        for t in temp:
            chk[t[0]] -= 1

    if ans != 'ERROR':
        for val in chk.values():
            ans = ans + str(val) +' '

    print(f'#{tc} {ans}')
