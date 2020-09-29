import sys
sys.stdin = open('swea4866.txt','r')

T=int(input())

for tc in range(1,T+1):
    input_list = list(input())
    chk = ['(', ')', '{', '}', '[', ']']
    chk2 = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack=[]
    for i in input_list:
        if i in chk:
            if len(stack) == 0:
                stack.append(i)
            else:
                temp = stack.pop(-1)
                if chk2.get(temp) == i:
                    continue
                else:
                    stack.append(temp)
                    stack.append(i)
    print(f'#{tc} {1 if len(stack)==0 else 0}')

