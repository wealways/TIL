import sys

for i in range(1,6):
    sys.stdin = open("in{0}.txt".format(i))
    arr = list(input())

    answer = ''
    stack = []
    for a in arr:
        if ord(a)>=48 and ord(a)<=57:
            answer += a
        else:
            if a == '(':
                stack.append(a)
            elif a in ['+','-']:
                while stack and stack[-1] != '(':
                    answer += stack.pop()
                stack.append(a)
            elif a in ['*','/']:
                while stack and stack[-1] in ['*','/']:
                    answer += stack.pop()
                stack.append(a)
            elif a == ')':
                while stack and stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()
    while stack:
        answer += stack.pop()
    print(answer)
    sys.stdin = open("out{0}.txt".format(i))
    print(input())

    

