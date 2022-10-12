import sys
from collections import deque

for i in range(1,6):
    sys.stdin = open("in{0}.txt".format(i))
    m,k = map(int,input().split())

    people = deque([i+1 for i in range(m)])

    cnt = 0
    while len(people)!=1:
        cnt += 1
        person = people.popleft()
        if cnt % k !=0:
            people.append(person)
    print(people[0])
    sys.stdin = open("out{0}.txt".format(i))
    print(input())