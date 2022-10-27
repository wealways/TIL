# Queue

큐 : python queue 바리으러리

- queue 라이브러리에는 다양한 큐 구조로 `Queue()` , `LifoQueue()`, `PriorityQueue()` 제공
- 프로그램을 작성할 떄 프로그램에 따라 적합한 자료 구조를 사용
  - Queue() : 가장 일반적인 큐 자료구조
  - LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조  (= 스택 구조)
  - PrioritQueue() : 데이터마다 우선순위를 넣어서 우선순위가 높은 순으로 데이터 출력



리스트로 queue 구현하기

```python
queue=list()

def enqueue(data):
    queue.append(data)

def dequeue(data):
    data = queue[0]
    del queue[0]
    return data

```

