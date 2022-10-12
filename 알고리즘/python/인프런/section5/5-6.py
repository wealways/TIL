import sys
from collections import deque

for i in range(1,6):
    sys.stdin = open("in{0}.txt".format(i))
    n,m = map(int,input().split())
    people = deque([[d,0 if i!=m else 1] for i,d in enumerate(list(map(int,input().split())))])

    cnt = 0
    while True:
        person = people.popleft()
        flag = True
        for p in people:
            if person[0]<p[0]:
                flag = False
                break
        
        if flag == False:
            people.append(person)
        else:
            cnt += 1
            if person[1] == 1:
                break
    print(cnt)



    sys.stdin = open("out{0}.txt".format(i))
    print(input())
    print('--')
