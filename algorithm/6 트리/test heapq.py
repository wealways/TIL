import heapq

data= [8,10,7,5,4,6,9]
data1 = [8,10,7,5,4,6,9]
heap=[]

for c in data:
    heapq.heappush(heap,c)
    print(heap)
print()
heapq.heapify(data1)
print(data1)
print()
print('가장 작은 값 수정')
#가장 작은 값 수정
print(f'원래 힙 : {heap}')
heapq.heapreplace(heap,3)
print(f'가장 작은 값 3으로 수정 {heap}')
heapq.heapreplace(heap,11)
print(f'가장 작은 값 11로 수정 {heap}')

print('\n가장 작은 값 추출')
t= heapq.heappop(heap)
print(t,heap)

print('\n큰값 n개 구하기')
t= heapq.nlargest(2,heap)
print(t,heap)

print('\n작은값 n개 구하기')
t= heapq.nsmallest(2,heap)
print(t,heap)