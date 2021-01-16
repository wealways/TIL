# 코드

> 순서 : 가상환경 생성 -> 필요한 패키지 다운( django 필수)-> 프로젝트 , 앱 생성 및 설정 -> model 생성 (DB)
>
> ->  __템플릿,url 분리__  ->  **CRUD**

## ◾ url, 템플릿 분리

확장성을 위해 두개를 분리할거에요.

### URL 분리

- 프로젝트 url 분리

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

- 앱 url 생성

```python
# articles/urls.py

from django.urls import path

app_name = 'articles'
urlpatterns = [
  ...
]
```

### 템플릿

- `base.html` 설정

```django
<!-- crud/templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="<https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css>"
    integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
    
  <div class="container"> 
    {% block content %}
    {% endblock %}
  </div>
    
  <script src="<https://code.jquery.com/jquery-3.5.1.slim.min.js>"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous">
  </script>
  <script src="<https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js>"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
  </script>
  <script src="<https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js>"
    integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous">
  </script>
</body>
</html>
```

- settings 설정

```python
# project/settings.py

'DIRS': [BASE_DIR / 'project' / 'templates'],
```



## ◾ CRUD

>  Create, Read, Update, Delete 4가지 기능은 어떤 앱을 만들든 지 필수적으로 들어가야하는 것들입니다. Django기반으로 instagram을 예로 들어볼게요.
>
> 1. 포스팅을 하려면 Create가 필요해요. 
>
> 2. 조금 더 디테일하게 포스팅을 보려면 Read가 필요하죠. 
>
> 3. 글을 수정하려면 Update도 해야하구요. 
>
> 4. 마지막으로 포스팅을 삭제하려면 Delete 또한 필요한 기능이죠.
>
> 추가적으로 팔로우하거나 좋아요를 누르거나, 검색을 하는등.. 이런 기능들은 CRUD를 바탕으로 만들어지는 것이기 때문에.. 조금 나중에 배워보도록 해요.

### INDEX

- url

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```

- view

```python
# articles/views.py

def index(request):
    return render(request, 'articles/index.html')
```

- template

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
{% endblock %}
```

### CREATE







