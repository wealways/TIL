# Array

파이썬에서는 리스트 타입의 자료구조를 제공함

- 장점
  - 빠른 접근 가능 : 첫 데이터의 위치에서 상대적인 위치로 데이터 접근 (인덱스 번호로 접근)
- 단점
  - 데이터 추가/삭제 어려움 : 미리 최대길이를 지정해야 함.

### 1차원 배열

```python
# 1차원 배열
single_list = [1,2,3,4,5]
print('single list 접근: %d' % single_list[0])
```

### 2차원 배열

```python
double_list = [[1,2,3],[4,5,6]]
print('double_list 접근: %d' % double_list[0][1])
```

