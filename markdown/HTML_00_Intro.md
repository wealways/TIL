# HTML이란?

Hyper Text Markup Language

> "웹 컨텐츠의 의미와 구조를 정의할 때 사용하는 언어"



이전에는 페이지가 순서대로 넘어가야 했었어요. 근데 이제, http ( hyper text transfer protocal) 이제 링크를 누르면 넘어갈 수 있게 바뀌었답니다!

## 0 설정

<img src="https://recipe1.ezmember.co.kr/cache/recipe/2019/02/03/666b4626b35c8ed65abeaec3276e163a1.jpg" alt="지글지글" style="zoom:10%;" /> [사진출처](https://www.10000recipe.com/recipe/6905834)
지글지글 본격 HTML 하기 `전` 굽기~~ 

### 0.1 vscode extension
- open in browser
- auto rename tag
- highlight matching tag

### 0.2 vscode settings 변경
`ctrl + shift +p`  > `open settings(JSON)`  > 아래 코드 추가

```json
"editor.tabSize": 2,
"[python]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true
}
```



## 1 개념

### 1.1 Hyper

- 텍스트 등의 정보가 동일 선상에 있는 것이 아니라 다중으로 연결되어 있는 상태

### 1.2 Hyper Text

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근 할 수 잇는 텍스트
- 하이퍼 텍스트가 쓰인 기술등 중 가장 중요한 2가지 (http, html)

### 1.3 Markup Language

- 특정 텍스트에 역할을 부여하는, 따라서 "마크업을 한다" 라고 하는 건 제목이 제목이라하고 본문이 본문이라고 마킹을 하는 것
- ex) h1 tag는 단순히 글자가 커지는 것이 아니라 의미론적으로 그 페이지에서 가장 핵심 주제를 의미하는 것

## 2 HTML 기본 구조

```html
<! DOCTYPE html>
<html lang ="ko">
    <head>  
        <meta charset = 'utf-8'>
        <title>Document</title>
    </head>
    <body>
        
        
    </body>
</html>
```

### 2.1 DOM

- DOM은 문서의 구조화된 표현(structured representation)을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
- DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
- 웹 페이지의 객체 지향 표현

### 2.2 요소 (Element)

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(Element, 요소)는 컨텐츠(내용)를 감싸서 그 정보의 성격과 의미를 정의 한다.
- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있다.

### 2.3 속성 (Attribute)

- 속성(Attribute)은 태그의 부가적인 정보가 들어온다.
- 요소는 속성을 가질 수 있으며 요소에 추가적 정보(이미지 파일의 경로, 크기 등)를 제공한다. 
- 요소의 시작 태그에 위치해야 하며 **이름**과 **값**의 쌍을 이룬다.
- 태그와 상관없이 사용 가능한 속성들(html global attribute)도 있다.

## 3 시맨틱 태그

> 브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 태그

### 3.1 장점

1. 읽기 쉬워진다. (개발자)
   - 개발자가 의도한 요소의 의미가 명확히 드러나고 있다.이것은 코드의 가독성을 높이고 유지보수를 쉽게 한다.
2. 접근성이 좋아진다. (검색엔진 및 보조기술 → 시력장애용 스크린리더 → 더 나은 경험 제공)
   - HTML 문서는 html 언어 + 사람이 읽을 수 있는 content의 조합인데, 검색 엔진은 HTML 코드만 잘 읽는다.
   - 그래서 이 검색 엔진이 HTML을 잘 이해하도록 시맨틱 태그 사용이 권장되고, 그러면 검색 엔진도 무슨 내용인지 이해할 수 있게 된다.

### 3.2 대표적인 태그

`header` : 문서 전체나 섹션의 헤더 (머릿말 부분)

`nav` : 네비게이션

`aside` : 사이드에 위치한 공간, 메인콘텐츠와 관련성이 적은 콘텐츠

`section` : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현 

`article` : 문서,페이지, 사이트 안에서 독립적으로 구분되는 영역

`footer` : 문서 전체나 섹션의 마지막부분

### 3.3 시맨틱 웹

> 웹에 존재하는 수많은 웹페이지들에 메타데이터를 부여하여, 기존의 단순한 데이터 집합이었던 웹페이지를 '의미'와 '관련성'을 가지는 거대한 데이터베이스로 구축하고자 하는 발상.



## 팁
### emmet
`option*5` 
```html
<option></option>
<option></option>
<option></option>
<option></option>
<option></option>
```

