import sys
sys.stdin = open('swea4874.txt','r')

T = int(input())
for tc in range(1,T+1):
    input_list = list(input().split())
    stack1=[]
    operator = ['+','-','*','/','.']
    try:
        for i in input_list:
            if i not in operator:
                stack1.append(i)
            else:
                if i == '.':
                    ans = stack1.pop()
                    break
                num2, num1 = int(stack1.pop()), int(stack1.pop())

                if i == '*':
                    temp = num1 * num2
                    stack1.append(temp)
                elif i =='/':
                    temp = num1 // num2
                    stack1.append(temp)
                elif i =='+':
                    temp = num1 + num2
                    stack1.append(temp)
                elif i =='-':
                    temp = num1 - num2
                    stack1.append(temp)

    except:
        ans = 'error'

    if len(stack1) >= 1:
        ans = 'error'

    print(f'#{tc} {ans}')