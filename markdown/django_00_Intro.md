# django_00_Intro

>python 오픈소스 웹 프레임워크이자 풀 스택 프레임워크입니다. D는 묵음입니다. 쟝고에요 쟝고!
>
>MTV 방식입니다 (대부분은 MVC방식!, 이름만 다를뿐 개념은 같다)

<img src="../images/til/django_00_Intro_mtv.PNG" style="zoom:50%;" />

| 기존       | Django   | 하는 일                                                      |
| :--------- | -------- | ------------------------------------------------------------ |
| Model      | Model    | DB에 저장되는 테이블 구조를 정의                             |
| View       | Template | 사용자에게 보여지는 UI                                       |
| Controller | View     | 프로그램의 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 template과 결합하여 전달 |

## 0 설정

시작하기에 앞서 `세팅 전` 구워주겠습니다.🍳



### ◾ django 설치하기

> 파이썬 3.7.7 설치되어 있어야합니다. (3.5버전은 장고2가 설치가 되버립니다.)

```bash
$ pip install django #최신버전설치
$ pip install django==2.1.0  #특정버젼 설치하기
```



### ◾ vscode 설정

1. django extension 설치하기
2. open settings(JSON) 들어가서 복붙

```json
"files.associations": {     
    "**/*.html": "html",     
    "**/templates/**/*.html": "django-html",     
    "**/templates/**/*": "django-txt",     
    "**/requirements{/**,*}.{txt,in}": "pip-requirements" }, 
 
"emmet.includeLanguages": {"django-html": "html"}
```



지글지글 전굽기 완료....? [사진출처](https://www.10000recipe.com/recipe/6905834)

<img src="../images/setting.jpg" alt="세팅전굽기" style="zoom:25%;" />



## 1 django Intro

> 다음의 순서대로 django 프로젝트를 진행합니다.

### ◾ bash환경

1. 프로젝트 만들기

```
django-admin startproject 프로젝트이름 입력
```

```bash
$ django-admin startproject first_project
```

2. 서버 실행하기

```bash
# manage.py가 있는 폴더
$ python manage.py runserver
```

3. 앱 생성하기

```
$ python manage.py startapp 앱이름
```

```bash
$ python manage.py startapp articles
```

✅앱 이름에 `-` 사용할 수 없고, 파이썬이나 장고에서 이미 쓰이는 이름을 쓰면 안됩니다.

✅앱을 생성하면 앱이름을 가진 폴더가 생기고 그 안에 부수적으로 views.py , models.py 등의 파일들이 자동으로 생성됩니다.

### ◾ django python 내부

4. 앱 프로젝트에 등록하기

`settings.py`

```python
INSTALLED_APPS = [     
#내가 만든 apps     
'articles',          
'django.contrib.admin',     
'django.contrib.auth',     
'django.contrib.contenttypes',     
'django.contrib.sessions',     
'django.contrib.messages',     
'django.contrib.staticfiles', ]
```

✅ settings.py 파일에서 Installed_apps 에 내가 방금 만든 app 이름을 상단에 추가한다.

✅ settings.py 파일 최하단에 LANGUAGE_CODE = 'ko-kr' 로 바꾸면 한글 설정이 된다

✅ TIME_ZONE = 'Asia/Seoul' 시간 설정도 바꿀 수 있다



### ◽ 참고사항

❗ startapp으로 앱 생성 후 settings.py 에 앱 등록 (반대 순서로 진행하지 않게 주의 )

❗ django에는 trailing comma이다. 코드뒤에 아무 것도 없어도 `,` 를 붙인다. 



## 2 django 개발

> 장고를 설치했고, 앱까지 만들어서 등록을 해봤습니다. 이제 본격적으로 `MTV`방식을 적용해보기로 하죠.
>
> 다음과 같은 개발 순서를 가지며, 실제로 http request를 받아서 처리하는 순서와 동일합니다.
>
> `urls.py` > `views.py` > `templates`

### ◾ url.py

```python
from django.contrib import admin 
from django.urls import path
from articles import views #1
 
urlpatterns = [     #2
    path('admin/', admin.site.urls), 
    path('index/', views.index), #3
]
```

✅  #1 주소를 추가하는 과정입니다. `articles` 앱에 있는 `views.py` 가져온거 보이시죠?

✅  #2  `urlpatterns` 안에 `path` 로 주소를 추가한다. 

✅  #3 `path()` 의 첫 번째 인자로는 유저가 리퀘스트를 보낼 `주소`를 적고 두 번째 인자로는 리턴해 줄 `함수` 이름을 적는다. 

❗ url 뒤에 `/` 을 까먹지 말고 붙여주자

❗ trailing comma 까먹지 말자

### ◾ views.py

```python
def index(request):  #1
    context = {  #3
        #dict
    }
    return render(request,'index.html',context) #2
```

✅ #1위와 같이 사용자가 `특정 url` 에 접속했을 때 불러질 함수를 만든다. 이 때 함수의 첫 번째 인자는 `무조건 request` 이다. 

✅ #2 render() 를 사용하여 html 페이지를 리턴해주는데, 이 때도 render 의 첫 번째인자는 `무조건 request` 이다. 

✅ #2 두 번째 인자로는 `return 할 html 페이지명`을 적는다. 이 때, 장고에서는  앱/templates/ 위치에서 html 파일을 찾기로 정해져있기 때문에, 추가 적으로 경로를 적어줄 필요 없이 `파일명만` 적어주면 된다. 

✅ #3 `context` 는 return할 html에 `데이터를 보내주는 dictionary`이다.

> 마지막으로 앱 안에 `templates` 라는 이름을 가진 폴더를 생성하고, `그 안에서 html 파일>을 작업` 해야한다



### ◾ templates : 반환 html 만들기

✅ 앱/templates/ 위치에서 반환해줄 html 페이지 템플릿을 생성한다. 

✅  파일명을 render() 함수 두 번째 인자와 같게 설정하면 된다



## 3 Django Template Language (DTL)

>django template system에서 사용하는 built-in template system이다.
>
>프로그래밍적 로직이 아니라 (이건 view에서 한다) 프레젠테이션을 표현하기 위한 것!
>

✅ 조건, 반복, 치환, 필터, 변수 등의 기능을 제공.

❗ 파이썬처럼 if,for를 사용할 수 있지만 이것은 단순히 python code로 실행되는 것이 아니다.

### ◾ sytax

- variable: `{{  }}`
- filter:  `{{ variable|filter }}`
- tags:  `{% tag %}`

