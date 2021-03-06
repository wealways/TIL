# CSS란?

> Cascading Style Sheets
>
> 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어



## 1 CSS 구문

### 1.1 특징

- 스타일을 지정할 html 요소를 선택한다.
- 각 쌍은 우리가 선택한 요소의 속성을 지정하고 속성에 부여할 값을 지정한다.

### 1.2 선언

- 속성 (property)
  - 사람이 읽을 수 있는 식별자로, 어떤(글꼴,너비,배경색 등) 스타일 기능을 변경할 지 나타냅니다
- 값 (value)
  - 각 속성에는 값이 있다.
  - 값은 어떻게(글꼴은 이거, 배경색은 저거) 스타일 기능을 변경할 건지 나타냅니다.

```
selector(선택자) {
	property(속성) : 값(value);
}
```

예시

```css
h1{
    color: blue;
    font-size: 15px;
}
```

### 1.3 정의

- Inline style : 해당 태그안에 직접 입력

- 내부참조

  ```html
  <head>
      <style>
          h1 {
              color:blue;
              font-size: 10px;
          }
      </style>
  </head>
  ```

- 외부참조

  ```html
  <head>
      <link rel="stylesheet" href="mystyle.css">
  </head>
  ```



## 2 CSS Selector

> HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요
>
> - 기초선택자
>   - 전체 선택자. 타입선택자
>   - 클래스 선택자, 아이디 선택자 속성 선택자
> - 고급 선택자
>   - 자식 선택자, 자손 선택자
>   - 형제,인접 형제 선태가
> - 의사 클래스(Pseudo class)
>   - 링크,동적 의사 클래스
>   - 구조적 의 사 클래스

### 2.1 클래스(class) 선택자

- 클래스 선택자는 마침표( .) 문자로 시작 하며 해당 클래스가 적용된 문서의 모든 항목을 선택

### 2.2 아이디(id) 선택자

- 아이디 선택자는 `#` 문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용
- 그러나 아이디는 문서 당 한 번만 사용할 수 있으며 요소에는 단일 id값만 적용 할 수 있다
- 문서에서 동일한 아이디를 여러 번 사용해도 동작하나 그렇게 하면 안된다

### 2.3 복합선택자

- 자손: 하위의 모든 요소 / selector1 `공백` selector2
- 자식: 바로 아래 요소 /  selector1 `>` selector2

### 2.4 적용 우선순위

1. `!important`
   - 다른 사람들의 코드에서 발견할 때 그 의미를 알 수 있는 것은 좋다.
   - 하지만 반드시 필요한 경우가 아니면 절대 사용하지 않는 것이 좋다.,
   - `!important` 는 cascading이 정상적으로 작동하는 방식을 변경하므로, CSS 스타일 문제를 해결하기가 어렵습니다.
2. inline style
3. id 선택자
   - id는 대부분의 다른 선택자보다 우선순위가 높기 때문에 다루기가 어려워 질 수 있다.
   - 대부분의 경우 id 보다는 모두  class 선택자로 작성하는 것이 좋다.
   - 만약 문서 내 `링크 이동`이나 `for`를 사용하는 특별한 경우에만 아이디를 사용한다.
4. class 선택자
5. 요소 선택자
6. 소스 순서

### 2.5 상속

"css는 상속을 통해 부모 요소의 속성을 ~~모두~~ 자식에게 상속한다."

- 속성 중에는 상속되는것과 안되는 것이 있다.
- 상속되는 것 예시
  - text관련 요소 (font, color, text-align), opacity,visibility 등
- 상속되지 않는 예시
  - Box model 관련 요소 (width,height, margin, padding, border ....)
  - position 관련 요소 (position, top/right/bottom/left,..)

## 3 CSS 단위

### 3.1 (상대)크기 단위

> 기본값 16px == 1em == 100% 

- px
  - 모니터 해상도의 한 화소인 '픽셀'을 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - `가변적인 레이아웃`에서 자주 사용
- em
  - em은 상속의 영향을 받음
  - 부모의 상대크기 설정 후 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - 최상위요소(html)을 절대 단위 기준으로 삼음. 상속의 영향을 받지 않음
  - 그래서 대부분 이걸 많이 사용함
- viewport
  - (스크롤을 내리지 않은 상태에서) 웹 페이지를 방문한 유저에게 현재 보이는 웹 컨텐츠의 영역
  - viewport 기준으로 한 상대적인 사이즈
  - 주로 스마트폰, 테블릿 화면 vw,vh

### 3.2 색상 표현 단위

- 색상 키워드
  - 색상 키워드는 대소문자를 구분하지 않는 식별자로, red, blue, black처럼 특정 색을 나타낸다
- RGB 색상
  - 빨강, 초록, 파랑을 통해 특정 색을 표현
  - 16진수 표기법이나 함수형 표기법으로 사용
  - a는 alpha(투명도)가 추가된 것
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색상을 표현
  - a는 alpha(투명도)가 추가된 것