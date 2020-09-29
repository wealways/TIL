import sys
sys.stdin = open('swea5177.txt','r')
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value

    cur = heapcount
    p = cur//2
    while p and heap[p] > heap[cur]:
        heap[p],heap[cur] = heap[cur],heap[p]
        cur = p
        p= cur//2
T= int(input())
for tc in range(1,T+1):
    N =int(input())
    input_list = list(map(int,input().split()))
    heap = [0] * (N + 1)
    heapcount=0
    for i in range(N):
        heappush(input_list[i])
    sumv=0
    while True:
        N = N//2
        sumv += heap[N]
        if N==0:
            break
    print('#{} {}'.format(tc,sumv))

'''
import heapq

for tc in range(1,T+1):
    N =int(input())
    input_list = list(map(int,input().split()))
    heapq.heapify(input_list)
    heap=[0]+input_list
    sumv=0
    while True:
        N = N//2
        sumv += heap[N]
        if N==0:
            break
    print(sumv)
'''