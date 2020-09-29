# django_00_Intro

>python 오픈소스 웹 프레임워크이자 풀 스택 프레임워크입니다. D는 묵음입니다. 쟝고에요 쟝고!
>
>MTV 방식입니다 (대부분은 MVC방식!, 이름만 다를뿐 개념은 같다)

<img src="../images/til/django_00_Intro_mtv.PNG" style="zoom:50%;" />

## ◾ 프로젝트

### 1. 개념

>  모든것을 총괄하는 MTV, 어플리케이션들의 집합 

| 기존       | Django       | 하는 일                                                      |
| :--------- | ------------ | ------------------------------------------------------------ |
| Model      | **Model**    | DB에 저장되는 테이블 구조를 정의                             |
| View       | **Template** | 사용자에게 보여지는 UI                                       |
| Controller | **View**     | 프로그램의 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 template과 결합하여 전달 |

### 2. 구조

- `__init__.py`
  - 빈 파일
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
- `settings.py`
  - 웹사이트의 모든 설정을 포함
  - 우리가 만드는 어떤 application이라도 등록이 되는 곳이며, static files의 위치, database 세부 설정 등이 작성
- `urls.py`
  - 사이트의 url와 view의 연결을 지정
- `wsgi.py`
  - Web Server Gateway Interface
  - 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 도움
- `asgi.py`
  - new in 3.0
  - Asynchronous Server Gateway Interface
  - 장고 어플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

## ◾ 어플리케이션

### 1. 개념

> 실제로 어떠한 역할을 해주는 것, 실제 요청을 처리하고 페이지를 보여주고 하는 것이 어플리케이션의 역할

- 하나의 프로젝트는 여러 개의 app을 가질 수 있다.
  - app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
  - 그러나 작은 규모의 서비스에서는 잘 나누지 않는다. 
  - 반드시 이렇게 나눠야 한다 같은 기준 또한 없다.
- **일반적으로 app 이름은 `복수형`으로 하는 것이 좋다.**

### 2. 구조

- `admin.py`
  - 관리자용 페이지 관련 기능을 작성 하는 곳.
- `apps.py`
  - 앱의 정보가 있는 곳. 
  - 우리는 수정할 일이 없다.
- `models.py`
  - 앱에서 사용하는 Model(Database)를 정의하는 곳.
- `tests.py`
  - 테스트 코드를 작성하는 곳.
- `views.py`
  - view가 정의 되는 곳. 

## ◾ 기본적인 요청 응답 순서

1. 장고 서버로 요청(request)이 들어오면, `urls.py`에서 그 요청이 어디로 가야하는 지 인식하고 관련된 함수(View)로 넘겨준다.
2. `views.py`에서는 요청에 알맞는 함수를 실행하여, Model이나 Templates를 통해 요청에 대한 행동을 한다.
3.  Templates
   - Django에서 template이라고 부르는 HTML파일은 기본적으로 app 폴더 안의 templates 폴더 안에 위치한다.
4. Model
   - 모델은 단일한 데이터에 대한 정보를 가지고 있어서 요청에 따라 데이터를 저장하거나 추출하고 응답하기도 한다.

## ◾ Template

### 1. 개념

> Django에서 유저들에게 보여주기 위해 활용하는 HTML 파일

[참고1](https://docs.djangoproject.com/ko/3.1/topics/templates/#context)

### 2. Templates Variable

- `render()`함수를 사용하여 View에서 정의한 변수를 Template로 넘겨서 사용함
- `context = {'key':value}` 와 같은 딕셔너리 형태로 넘겨주며 여기서 `key`에 해당하는 문자열에 template에서 사용가능한 변수명이 된다. 

### 3. Variable Routing

> 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것

[참고](https://docs.djangoproject.com/en/3.1/topics/http/urls/#path-converters)

- ```python
  #urls.py
  urlpatterns = [
  	path('<int:article_pk>/update/',views.update),
  ]
  # views.py
  def update(request,article_pk):
      ....
  ```

### 4. Django Template Language

> django template system에서 사용하는 built-in template system이다.
>
> 프로그래밍적 로직이 아니라 (이건 view에서 한다) 프레젠테이션을 표현하기 위한 것!

- 파이썬처럼 if,for를 사용할 수 있지만 이것은 단순히 python code로 실행되는 것이 아니다.

**syntax**

- variables : `{{  }}`
  - context에서 값을 출력하는데, context는 키를 값에 매핑하는 딕셔너리와 유사한 객체
- tags : `{% tag %}`
- filters : `{{ variable|filter }}`
  - 변수 및 태그 인수의 값을 변환
- comments

[참고1](https://docs.djangoproject.com/ko/3.1/ref/templates/language/#tags)

[참고2](https://docs.djangoproject.com/ko/3.1/ref/templates/builtins/#built-in-template-tags-and-filters)

## ◾ Model

> 단일한 **데이터에 대한 정보**를 가지고 있다.

### 1. 개념

- 필수적인 필드(컬럼)와 데이터(레코드)에 대한 정보를 포함한다.
- 일반적으로 각각의 **모델(클래스)**는 단일한 데이터베이스 **테이블과 매핑**된다.
- 모델은 부가적인 메타데이터를 가진 **DB의 구조(layout)를 의미**
- 사용자가 저장하는 **데이터들의 필수적인 필드와 동작(behavior)** 포함

### 2. DB 기본 구조

- 데이터베이스 (DB)

  - 체계화된 데이터의 모임

- 쿼리(Query)

  - 데이터를 조회하기 위한 명령어
  - (주로 테이블형 자료구조에서) 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - Query를 날린다 → 데이터를 DB에 요청 → 응답 데이터는 QuerySet (Model의 인스턴스)

- 스키마 (Schema) / 뼈대(Structure)

  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
  - 데이터베이스 관리 시스템(DBMS)이 주어진 설정에 따라 데이터베이스 스키마를 생상하며, 데이터베이스 사용자가 자료를 저장, 조회, 삭제, 변경할 때 DBMS는 자신이 생성한 데이터베이스 스키마를 참조하여 명령을 수행

- 테이블 (Table) / 관계(Relation)

  - 필드(field): 속성, 컬럼(Column)

    - 모델 안에 정의한 클래스에서 클래스 변수가 필드가 된다.

  - 레코드(record): 튜플, 행(Row)

    - 우리가 ORM을 통해 해당하는 필드에 넣은 데이터(값)을 의미한다.

### 3. ORM

> "Object-Relational-Mapping 은 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에(Django - SQL)데이터를 변환하는 프로그래밍 기술이다. 이것은 프로그래밍 언어에서 사용할 수 있는 '가상 객체 데이터베이스'를 만들어 사용한다."

- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법이다. 객체 관계 매핑이라고도 부른다.
- 객체 지향 언어에서 사용할 수 있는 '가상' 객체 데이터베이스를 구축하는 방법이다.
- 현대 대부분의 프레임워크는 ORM 사용
- 장점
  - SQL을 몰라도 DB 연동이 가능하다. (SQL 문법을 몰라도 쿼리 조작 가능)
  - SQL의 절차적인 접근이 아닌 객체 지향적인 접근으로 인해 `생산성`이 증가한다.
  - ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용할 수 있다. 때문에 모델에서 가공된 데이터를 컨트롤러(view)에 의해 뷰(template)과 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어렵다.
  - 프로젝트의 복잡성이 커질 경우 설계 난이도가 상승할 수 있다.

**정리**

- 객체 지향 프로그래밍에서 DB를 편리하게 관리하게 위해 ORM 프레임워크를 도입
- **"우리는 DB를 객체(object)로 조작하기 위해 ORM을 사용한다."**

## ◾ CRUD

### 1. 개념

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말

> 이러한 4개의 조작을 모두 할 수 없다면 그 소프트웨어는 완전하다고 할 수 없다. 
>
> 이들 기능은 매우 기본적이기 때문에, 한 묶음으로 설명되는 경우가 많다.

[참고](https://ko.wikipedia.org/wiki/CRUD)

## ◾ Admin

### 1. 개념

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Article class를 `admin.py` 에 등록하고 관리
- `django.contrib.auth` 모듈에서 제공하는 것 → Django에서 제공되는 Authentication 인증 프레임워크
- record 생성 여부 확인에 매우 유용하고 CRUD 로직을 확인하기에 편리하다.

