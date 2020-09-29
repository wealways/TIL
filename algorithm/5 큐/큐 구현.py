
# front, rear 이용하자
Q = [0]* 100
front, rear = -1,-1
def enQueue(item):
    global rear
    if rear == len(Q)-1:
        print('Queue 꽉 참')
    else:
        rear = rear + 1
        Q[rear] = item

def deQueue():
    global front
    if front ==rear:
        print('Queue 비었음')
    else:
        front += 1
        return Q[front]
def qpeek():
    if front == rear:
        print('Queue empty')
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)