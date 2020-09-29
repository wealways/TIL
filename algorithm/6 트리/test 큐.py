from collections import deque

Q = deque()
for i in range(10):
    Q.append(i)

print('1',Q)
t=Q.popleft()
print('2',t,Q)
t=Q.pop()
print('3',t,Q)

print('\n시간적손해')
lst=[]
lst.append(10)
lst.pop()