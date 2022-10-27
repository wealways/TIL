# Stack

스택 : 리스트로 stack 구현하기

```python
stack = list()

def push(data):
    stack.append(data)
    
def pop():
    data = stack[-1]
    del stack[-1]
    return data
```

