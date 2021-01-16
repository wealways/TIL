# Data structure

데이터 구조란 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법을 말합니다.

> Program = Data structure + Algorithm

- 순서가 있는 구조
  - 문자열
  - 리스트
- 순서가 없는 구조
  - 세트
  - 딕셔너리

<br>

## ◾ 문자열

>  변경할 수 없고 (immutable), 순서가 있고(ordered), 순회가능하다(iterable)

### 조회 및 탐색

- `.find(x)` : x의 첫번째 위치를 반환합니다. 없으면 `-1`을 반환합니다.
- `.index(x)` : x의 첫번째 위치를 반환합니다. 없으면 오류가 발생합니다.

### 값 변경

- `.replace(old,new[,count])` : 바꿀 old 글자를 new로 바꿉니다. [count]만큼 시행합니다.

  ```python
  'wooooowoo'.replace('o', '', 2)
  >>> 'wooowoo'
  ```

- `.strip([chars])` : 특정문자를 지정하면, 양쪽을 제거하거나 왼쪽(lstrip), 오른쪽(rstrip)을 제거합니다.

- `.split()` : 문자열을 특정단위로 나누어 `리스트`로 반환합니다.

- `'separator'.join(iterable)` : 반복가능한(iterable) 컨테이너 요소들을 separator로 합쳐서 `문자열`로 반환

  ```python
  word = '배고파'
  words = ['안녕', 'hello']
  '!'.join(word)
  >> '배!고!파'
  ' '.join(words)
  >> '안녕 hello'
  ```

### 문자변형

- `.capitalize()` :앞글자를 대문자로!
- `.title()` : 공백이후의 문자를 대문자로!
- `.upper()` : 모두다 대문자로!
- `.lower()` : 모두 소문자로!
- `.swapcase()` : 대문자는소문자,소문자는대문자

<br>

## ◾ 리스트

> 변경가능하고 (mutable), 순서가 있고(ordered), 순회가능한(iterable)

### 값 변경

- `.append(x)`: 리스트에 x값을 추가합니다. 

- `.extend(iterable)` : 리스트에 __iterable(list, range, tuple, string)__ 추가!!

  ```python
  cafe = ['커피','우유']
  cafe.append('자허블')
  >> cafe = ['커피','우유','자허블']
  cafe.extend(['마끼아또'])
  >> cafe = ['커피','우유','자허블','마끼아또']
  
  #주의
  cafe.extend('허브차')
  >> cafe = ['커피','우유','자허블','마끼아또','허','브','차']
  ```

- `.insert(i,x)` : i 위치에 x를 추가합니다

- `.remove(x)` : 리스트에서 x를 삭제합니다

- `.pop(i)`: 정해진 위치 i에서 값을 pop해줍니다

### 탐색 및 정렬

- `.index(x)` : x가 없으면 에러가 발생합니다.
- `.count(x)`: x의 갯수를 확인합니다.
- `.sort()` : 정렬을 합니다. __원본을 변경__시키며 반환하는게 없습니다.  `sorted(list)` 는 return존재
- `.reverse()` : 반대로 뒤집습니다.

### 리스트활용하기

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'
result = [x for x in words if x not in vowels]
print(''.join(result))

>>> Lf s t shrt, y nd pythn!
```

<br>

## ◾ 순회가능한 데이터 구조에 적용가능한 함수

> iterable 타입 - `list`, `dict`, `set`, `str`, `btyes`, `tuple`, `range`

### map()

> map(function, iterable )
>
> 순회가능한 데이터 구조의 모든 요소에 function을 적용한 후 그 결과를 돌려준다.
>
> return 은 map_object 형태이다.

```python
def cube(n):
    return n**3
list(map(cube,[1,2,3]))

>> [1,8,27]
```

### filter()

> filter(function, iterable)
>
> 순회가능한 데이터에서 function의 반환된 결과가 `true` 인것들로만 반환한다.
>
> return 은 filter object이다

```python
def odd(n):
    return n%2
list(filter(odd,[1,2,3]))

>> [1,3]
```

### zip()

> zip(*iterables)
>
> 복수의 iterable 객체를 모아 `zip()` 해준다
>
> 결과는 튜플모음으로 구성된 zip object 입니다.

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david','hou']
pair = list(zip(girls, boys))

>> [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```

<br>

## ◾ 세트

> 변경가능하고, 순서가 없고, 순회가능하다. {}

### 값 변경

- `.add(x)` : 추가

- `.update(*iterable)` : 여러가지 값을 추가합니다.

  ```python
  a = {'사과', '바나나', '수박'}
  a.update({'토마토', '토마토', '딸기'}, {'포도', '레몬'})
  
  >> {'레몬', '수박', '사과', '바나나', '딸기', '포도', '토마토'}
  ```

- `.remove(x)` : x 삭제. 없으면 에러

- `.discard(x)` : x 삭제. 없어도 에러발생하지 않음

- `.pop()`: 팝해준다.

<br>

## ◾ 딕셔너리

> 변경가능하고, 순서가 없고, 순회가능하다.
>
> {key:value}

### 조회

- `.get(key [,default])` : key를 통해 값을 가져옵니다. 없으면 default를 만듧니다.
- `.keys()`
- `.values()`
- `.items()`

### 값 변경

- `.pop(key [,default])` : key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 없으면 에러발생. 그래서 deafult 정의해야한다.
- `.update()` : 값을 제공하는 key value로 덮어씁니다.

### 활용

- 리스트가 주어질 떄, 각각의 요소의 개수를 vaule값으로 갖는 딕셔너리를 만드세요.

  ```python
  book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
  
  title_counter = {}
  for title in book_title:
      title_counter[title] = title_counter.get(title, 0) + 1
  
  >> {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
  ```

  