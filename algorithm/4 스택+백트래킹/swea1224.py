import sys
sys.stdin = open('swea1224.txt','r')

out_stack = {
    '(':3,
    '*':2,
    '/':2,
    '+':1,
    '-':1
}
in_stack = {
    '(':0,
    '*':2,
    '/':2,
    '+':1,
    '-':1
}





for tc in range(1,11):
    N = int(input())
    input_list = list(input())
    stack1 = []
    string=[]

    #step1
    for ch in input_list:
        # 피연산자이면 string에 바로 추가
        if ch not in ['(',')','+','-','*','/']:
            string.append(ch)
        # 연산자이면 일단 우선순위 같은거 다 따져야해
        else:
            # '('이면 일단 넣어야지
            if len(stack1)==0 or ch=='(':
                stack1.append(ch)
            # ')'이면 계속 출력해 '('나올때 까지
            elif ch==')':
                while True:
                    temp=stack1.pop()
                    if temp != '(':
                        string.append(temp)
                    else:
                        break;
                    # if stack1.pop()=='(':
                    #     break
            # '('이 아니면  top위치에 있는 것과 비교를 해야해
            else:
                # 스택안에서 top에 있는 연산자 < 바깥연산자간의 순위 라면, 스택안에 push
                if in_stack.get(stack1[len(stack1)-1]) < out_stack.get(ch):
                    stack1.append(ch)
                # 스택안의 top에 있는 연산자 >= 바깥연산자 순위 이라면, 바깥게 더 클 때 까지 pop
                else:
                    while True:
                        temp = stack1.pop()
                        if in_stack.get(temp) < out_stack.get(ch):
                            stack1.append(temp)
                            stack1.append(ch)
                            break;
                        else:
                            string.append(temp)


    #step2
    stack1=[]
    for s in string:
        if s not in out_stack.keys():
            stack1.append(s)
        else:
            if s == '+':
                stack1.append(int(stack1.pop()) + int(stack1.pop()))
            elif s == '*':
                stack1.append(int(stack1.pop()) * int(stack1.pop()))
    print(f'#{tc} {stack1[0]}')


