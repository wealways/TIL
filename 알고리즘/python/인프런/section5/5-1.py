import sys

sys.stdin = open("in5-1.txt")

number,m = map(int,input().split())
number = list(str(number))
answer = []

for n in number:
    while answer and answer[-1]<int(n) and m!=0:
        answer.pop()
        m -= 1
    answer.append(int(n))

while m != 0:
    answer.pop()
    m -= 1
for a in answer:
    print(a,end='')
print()