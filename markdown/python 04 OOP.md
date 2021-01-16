# OOP

Object 객체

Object Oriented Programming 객체지향프로그래밍

Class & Object  클래스와 객체

<br>

## ◾ 객체

> python에서 모든 것은 __객체__ 입니다.
>
> 모든 객체는 = __타입__ __속성__ __조작법(method)__ 을 가진다.
>
> | type    | attributes   | methods                          |
> | ------- | ------------ | -------------------------------- |
> | complex | .real, .imag |                                  |
> | str     | _            | .capitalize(), .join(), .split() |
> | list    | _            | .append(), .reverse(), .sort()   |
> | dict    | _            | .keys(), .values(), .items()     |

### 타입 과 인스턴스

| type | instance             |
| ---- | -------------------- |
| int  | 0, 1, 2              |
| str  | '', 'hello', '123'   |
| list | [], ['a', 'b']       |
| dict | {}, {'key': 'value'} |

```python
a=int(10)
> a는 객체이자 int타입의 인스턴스
```

__`type`__ 

공통된 속성과 조작법을 가진 객체들의 분류

__`instance`__ 

- 특정타입의 실제 데이터 예시이다.
- 파이썬에서 모든 것은 객체이고, 모든 객체는 특정타입의 인스턴스이다.

### 속성

속성(attribute)는 객체의 상태이자 데이터를 뜻한다.

<객체>.<속성>

```python
3+4j.real
3+4j.imag
> .real=3 , .imag=4 
```

### 메서드

특정 객체에 적용할 수 있는 행위이다.

<객체>.<조작법>()

```python
[3, 2, 1].sort()
> .sort()는 리스트의 메서드입니다.
```

<br>

## ◾ 객체 지향 프로그래밍

> Object가 중심이 되는 프로그래밍
>
> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나이다.
>
> 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다.

### 객체 중심의 장점

- 코드의 직관성
- 활용의 용이성
- 변경의 유연성

<br>

## ◾ 클래스와 객체

> `type`: 공통 속성을 가진 객체들의 분류(class)
>
> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드

### 클래스 생성

- 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능하다.
- `<클래스의 이름>`은 `PascalCase`로 정의한다.
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 정의된 함수는 **메서드(method)**로 불린다.

```python
class <클래스이름>:
    <메소드>
    
class Person:
    pass
print(type(Person))
>> <class 'type'>
```

### 인스턴스 생성

- 정의된 클래스(`class`)에 속하는 객체를 해당 클래스의 인스턴스(instance)라고 한다.
- `Person` 클래스의 인스턴스는 `Person()`을 호출함으로써 생성된다.
- `type()` 함수를 통해 생성된 객체의 클래스를 확인할 수 있다.
- `person1`은 사용자가 정의한(user-defined) `Person`이라는 데이터 타입(data type)의 인스턴스이다.

```python
# 인스턴스 = 클래스()
person1 = Person()
print(type(person1))

>> <class '__main__.Person'>
```

### 메서드 정의⭐⭐

- 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미한다.

```python
class Person:
    # 메서드(method)
    def talk(self):    # 인자로 self를 붙여줍니다.
        return '안녕'
    def eat(self, food):
        return f'냠냠 {food}'
    

```

#### 생성자메서드 

- constructor method

- 인스턴스 객체가 생성될 때 호출되는 함수 
- 생성자를 활용하면 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있다.

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```

#### 소멸자 메서드

- desrtuctor method
- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 함수.

```python
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

#### 속성 정의

- 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터를 의미한다

```python
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return f'안녕, 나는 {self.name}'
    
me = Person('메시호날두')
print(me.name)
>> 메시호날두
```

#### 매직메서드

- 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`라고 불립니다.
- 매직(스페셜) 메서드 형태: `__someting__`
- \_\_new\_\_, \_\_reduce\_\_ , \_\_reduce_ex\_\_ , \_\_repr\_\_ , \_\_rmod\_\_ , \_\_rmul\_\_ , \_\_setattr\_\_ , \_\_sizeof\_\_ , \_\_str\_\_ 

- `__str__(self)`

  - 특정 객체를 출력(`print()`) 할 때 보여줄 내용을 정의할 수 있음

  ```python
  class Person:
      def __str__(self):
          return '객체 출력(print)시 보여줄 내용'
  ```

#### self

- 인스턴스 자신
- Python에서 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계되었다.

<br>

## ◾ 인스턴스 & 클래스 변수⭐⭐

### 인스턴스 변수

- 인스턴스의 속성(attribute)
- 각 인스턴스들의 고유한 변수(데이터)
- 메서드 정의에서 `self.변수명`로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당

```python
class Person:

    def __init__(self, name):    # 인스턴스 메서드 (생성자) 
        self.name = name         # 인스턴스 변수
ronaldo = Peron('messi')
print(ronaldo.name)
>> messi
```

### 클래스변수

- 클래스의 속성(attribute)
- 해당 클래스의 모든 인스턴스가 공유
- 클래스 정의 내부에서 선언
- `클래스.변수명` 또는 `인스턴스.변수명`으로 접근(할당)

```python
class Person:
    species = 'soccer'

    def __init__(self, name):
        self.name = name

ronaldo = Peron('messi')
mourinho = Person('mourinho')
print(ronaldo.species)
> 'soccer'
print(mourinho.species)
> 'soccer'
mourinho.species='??'
print(mourinho.species)
> '??'
```

