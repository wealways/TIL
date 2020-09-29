# 큐의 단점(메모리 낭비) 극복하기 위해 원형큐를 사용한다.
# 이때, front 부분을 비워두는데, full과 empty를 구분하려고
# front, rear 이용하자
size= 4
Q = [0]* size
front, rear = 0,0

def enQueue(item):
    global rear
    if (rear + 1) % size == front: #full
        print('Queue 꽉 참')
    else:
        rear = (rear + 1) % size
        Q[rear] = item

def deQueue():
    global front
    if front ==rear:
        print('Queue 비었음')
    else:
        front = (front + 1) % size
        return Q[front]
def qpeek():
    if front == rear:
        print('Queue empty')
    else:
        return Q[(front+1) % size]

enQueue(1)
enQueue(2)
enQueue(3)
print(qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())
print(Q)
enQueue(5)
print(front,rear)