

<br>

# 코드

> 순서 : 가상환경 생성 -> 필요한 패키지 다운( django 필수)-> 프로젝트 , 앱 생성 및 설정 -> model 생성 (DB)
>
> ->  **Form 생성** (ModelForm 활용)

<br>

## ◾ Form 생성

### ModelForm

> 사용자가 작성한 데이터를 받아와서 DB에 저장하려면 Form이라는 것이 필요하다. 그리고 django에서는 FormClass를 사용할 수 있지만...
>
> [참고](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#creating-forms-from-models)

- FormClass 에서는 Model에서 이미 정의한 필드를 반복해서 정의해야 한다.
- 하지만 Model에 이미 필드를 정의했기 때문에 다시 필드 유형을 정의하는 것은 불필요하다.

그래서 ModelForm을 사용한다. ( 자동으로 DBmodel과 Form을 연결해준다.)

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title', 
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```

<br>

### Form class

> [참고](https://docs.djangoproject.com/ko/3.1/topics/forms/#working-with-forms)
>
> 음.. 보통은 ModelForm을 사용해요. 그치만 이게 기본이 되는 거니까 알아놓읍시다!

- Form을 생성하기 위해, Form클래스에서 파생된, `forms` 라이브러리를 import 하고 폼 필드를 생성한다.
- app 폴더에 `forms.py` 파일을 작성한다.

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    REGION_A = 'sl'
    REGION_B = 'dj'
    REGION_C = 'gj'
    REGION_D = 'gm'
    REGIONS = [
        (REGION_A, '서울'),
        (REGION_B, '대전'),
        (REGION_C, '광주'),
        (REGION_D, '구미'),
    ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect())
```

이렇게 모델에서 정의한 테이블 구조를 form에서도 다시 적어야하는 비효율적인 부분이 존재한다. 그러므로 ModelForm을 쓰자!

<br>

# -----------------------

<br>

# 개념

## ◽ Intro

> Form은 Django 프로젝트의 주요 유효성 검사 도구들 중 하나이며, 공격 및 우연한 데이터 손상에 대한 중요한 방어 수단이다.

- 우리는 지금까지 HTML form, input을 통해서 사용자로부터 데이터를 받았다.
- 이렇게 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시하며, 유효한 데이터에 대해 요구되는 동작을 수행하는 것을 "올바르게 하기" 위해서는 꽤 많은 노력이 필요한 작업이다.
- Django는 일부 과중한 작업과 반복 코드를 줄여줌으로써, 이 작업을 훨씬 쉽게 만든다.

<br>

## ◽ Django's role in forms

Django는 forms에 관련된 작업의 세 부분을 처리한다.

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로 부터 받은 데이터 수신 및 처리

이 모든 작업을 수동으로 수행하는 코드를 작성할 수 있지만 Django가 모든 작업을 처리 할 수 있다.

<br>

## ◽ Form Class

> `Form` 클래스는 Django form 관리 시스템의 핵심이다. Form 클래스는 form내 field들, field 배치, 디스플레이 widget, label, 초기값, 유효한 값과 (유효성 체크이후에) 비유효 field에 관련된 에러메시지를 결정한다.
>
> [참고](https://docs.djangoproject.com/ko/3.1/topics/forms/#working-with-forms)

### 선언

`Form` 을 선언하는 문법은 `Model` 을 선언하는 것과 비슷하고 같은 필드 타입을 사용한다. (또한, 일부 매개변수도 유사하다.)

### Outputting forms as HTML

> [참고](https://docs.djangoproject.com/ko/2.2/ref/forms/api/#outputting-forms-as-html)

- `as_p()` : 각 필드가 단락(paragraph)으로 렌더링
- `as_ul()` : 각 필드가 목록항목(list item)으로 렌더링
- `as_table()` : 각 필드가 테이블 행으로 렌더링

### form fields

입력 유효성 검사 논리를 처리하며 템플릿에서 직접 사용됨

### widget

> [참고](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#module-django.forms.widgets)

Django의 HTML input 요소 표현

- 하지만 위젯은 반드시 form fields에 할당 됨을 주의하자

- 위젯을 form fields와 혼동해서는 안된다

<br>

## ◽ ModelForm

> [참고](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#creating-forms-from-models)

Django에서는 model을 통해 Form Class를 만들수 있는 Helper(도우미)를 제공한다.

- ModelForm Helper 클래스를 사용하여 모델에서 form을 작성
- ModelForm은 일반 Form과 완전히 같은 방식(객체생성)으로 view에서 사용할 수 있다.

### 첫번째 방식

```python
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
                }
            )
        }
```

### 두번째 방식 (권장)

맨 위 코드 방식

<br>

## ◽ Form vs ModelForm

- Form
  - 어떤 모델에 저장해야 하는지 알 수 없기 때문에 유효성 검사를 하고 실제로 DB에 저장할 때는  `cleaned_data` 와 `article = Article(title=title, content=content)` 를 사용해서 따로 `.save()` 를 해야 한다.
  - Form Class가 `cleaned_data` 로 딕셔너리로 만들어서 제공해 주고, 우리는 `.get` 으로 가져와서 Article 을 만드는데 사용한다.
- ModelForm
  - django 가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의한다.
  - `forms.py` 에 Meta 정보로 `models.py` 에 이미 정의한  Article 을 넘겼기 때문에 어떤 모델에 레코드를 만들어야 할지 알고 있어서 바로 `.save()` 가 가능하다.

<br>

## ◽ Rendering fields manually

> [참고](https://docs.djangoproject.com/ko/3.1/topics/forms/#rendering-fields-manually)

### Form 분리

template에서 `{{ form }}` 으로 한번에 사용해서 커스터마이징이 힘들었는데, 다양한 방법으로 사용도 가능하다.

- Rendering fields manually

```django
<!-- articles/create.html --> 

<h1>CREATE</h1>
...
<hr>

<form action="" method="POST">
  {% csrf_token %}
  <div>
    {{ form.title.errors }}
    {{ form.title.label_tag }}
    {{ form.title }}
  </div>
  <div>
    {{ form.content.errors }}
    {{ form.content.label_tag }}
    {{ form.content }}
  </div>
  <button class="btn btn-primary">작성</button>
</form>
```

- Looping over the form’s fields (`{% for %}`)

```django
<!-- articles/create.html --> 

...

<hr>

<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    {{ field.errors }}
    {{ field.label_tag }}
    {{ field }}
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```

### Bootstrap Form

> [참고](https://getbootstrap.com/docs/4.5/components/forms/)

`form-group`, `form-control` 두 class name이 핵심이다.

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={
            'class': 'my-title form-control',
            'placeholder': 'Enter the title',
            'maxlength': 10,
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'my-content form-control',
            'rows': 5,
            'cols': 50,
        }),
        error_messages={
            'required': '내용 넣어라...'
        }
    )
```

```django
<!-- articles/create.html -->

...

<hr>

<h2>Bootstrap Form</h2>
<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    <div class="form-group">
      {{ field.errors }}
      {{ field.label_tag }} 
      {{ field }}
    </div>
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```

### Error message with Bootstrap

```django
<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    {% if field.errors %}
      {% for error in field.errors %}
        <div class="alert alert-warning" role="alert">{{ error|escape }}</div>
      {% endfor %}
    {% endif %}
    <div class="form-group">
      {{ field.label_tag }} 
      {{ field }}
    </div>
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```

<br>

## ◽ Django Bootstrap Library

### django-bootstrap4

> [참고](https://django-bootstrap4.readthedocs.io/en/latest/installation.html)
>
> [참고](https://pypi.org/project/django-bootstrap4/)

```bash
$ pip install django-bootstrap4
```

```python
# settings.py

INSTALLED_APPS = [
  ...
  'bootstrap4',
	...
]
```

```bash
$ pip freeze > requirements.txt
```

```django
<!-- articles/base.html -->

{% load bootstrap4 %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% bootstrap_css %}
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  {% bootstrap_javascript jquery='full' %}
</body>
</html>
```

```django
<!-- articles/update.html -->

{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
  ...
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form layout='horizontal' %}
    {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
  </form>
  ...
  {% endif %}
{% endblock %}
```

<br>

## ◽ View decorators

> [장고공식문서](https://docs.djangoproject.com/en/3.1/topics/http/decorators/#module-django.views.decorators.http)

### 데코레이터

- 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 `연장`하게 해주는 `함수`

- Django는 다양한 HTTP 기능을 지원하기 위해 뷰에 적용 할 수있는 여러 데코레이터를 제공

### Allowed HTTP methods

> 일치하지 않는 메서드 요청이라면 `405 Method Not Allowed` 에러를 발생

- **`require_http_methods()`**
  - view가 특정한 요청 method만 허용하도록하는 데코레이터

```python
from django.views.decorators.http import require_http_methods, require_POST


@require_http_methods(['GET', 'POST'])
def create(request):
    pass

  
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    pass
```

- **`require_POST()`**
  - view가 POST 메서드만 요청만 승인하도록 하는 데코레이터

```python
from django.views.decorators.http import require_http_methods, require_POST


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

