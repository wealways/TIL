import sys

sys.stdin = open('in{}.txt'.format(2))

code = list(map(int, input()))
N = len(code)
print(code)
code.append(-1)
answer = []
visit = []
def dfs(v):
    print(visit)
    if v == N:
        print(visit)
        temp = ''
        for data in visit:
            temp += chr(data+64)
        answer.append(temp)
        return
    else:
        for i in range(1,27):
            if code[v] == i:
                visit.append(i)
                dfs(v+1)
                visit.pop()
            elif i>=10 and code[v] == i//10 and code[v+1] == i%10:
                visit.append(i)
                dfs(v+2)
                visit.pop()

dfs(0)
print(answer)
print(len(answer))