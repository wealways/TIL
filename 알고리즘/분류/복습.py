import sys
sys.stdin = open('복습.txt')
input = sys.stdin.readline

N = int(input())

arr = list(input())
arr.pop()
nums = []
for _ in range(N):
    nums.append(int(input()))

answer = []
for a in arr:
    if 65<=ord(a)<=90:
        answer.append(nums[ord(a)-65])
    else:
        n1 = answer.pop()
        n2 = answer.pop()
        if a=='+':
            answer.append(n2+n1)
        elif a=='-':
            answer.append(n2-n1)
        elif a=='*':
            answer.append(n2*n1)
        elif a=='/':
            answer.append(n2/n1)
print('{:.2f}'.format(round(answer[0],2)))
            

# print(ord('A')) #65