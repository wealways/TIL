def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    current = heapcount
    parent = current//2

    # 부모노드값이 자식노드값보다 크면? swap 해줘야지! 나 지금 최소힙 만들고 있잖아
    # parent  and ~~ : parent 있는 이유, 루트노드가 아니고~ 라는 것을 표현한거야
    while parent and heap[parent] >heap[current]:
        heap[parent],heap[current] = heap[current],heap[parent]
        current = parent
        parent = current//2

def heappop():
    global heapcount
    retvalue = heap[1]
    heap[1] =heap[heapcount]
    heap[heapcount]=0
    heapcount -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heapcount: #오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child += 1
    # 자식노드가 존재하고, 부모노드 > 자식노드 라면 ? 스왑
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child += 1
    return retvalue


# 최소힙
heapcount= 0
temp = [7,2,5,3,4,6]
N = len(temp)
# 1차원으로 힙을 구현할거에요
heap=[0]*(N+1)
for i in range(N):
    heappush(temp[i])

for i in range(N):
    print(heappop(), end=' ')
print()