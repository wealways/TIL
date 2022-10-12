import sys

for i in range(1,6):
    sys.stdin = open("in{0}.txt".format(i))
    data =input()

    stack = []

    for d in data:
        if ord(d)>=48 and ord(d)<=57:
            stack.append(int(d))
        else:
            if d == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2+n1)
            elif d == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif d == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2*n1)
            elif d == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2/n1)
    print(stack[0])
    sys.stdin = open('out{0}.txt'.format(i))
    print(input())