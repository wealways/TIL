## selection sort 이용해서 문제 풀기


import sys
sys.stdin = open('4843.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    for i in range(N):
        if i % 2 ==0:
            min = i
            for j in range(i + 1, len(lst)):
                if lst[min] < lst[j]:
                    min = j
            lst[i], lst[min] = lst[min], lst[i]
        else:
            max = i
            for j in range(i + 1, len(lst)):
                if lst[max] > lst[j]:
                    max = j
            lst[i], lst[max] = lst[max], lst[i]
    print(lst)