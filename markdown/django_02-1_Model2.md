![](../images/til/django_02_model_dbapi.png)

# ORM

>  자주 사용되는 ORM 문법에 대해 조금 더 디테일하게 알아봅시다
>
> ORM을 쓰는 이유는 DB조작을 객체 지향 프로그래밍(클래스)처럼 하기 위해서 입니다!!



## \__str__

모든 모델마다 표준 파이썬 클래스의 메소드인 **str**() 을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환(return)하도록 한다.

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```



## ◾ Create

### 기초설정

- 정의한 테이블을 사용하기 위해서는, `import`해서 가져오는게 필요합니다.

```python
from .models import Article

Article.objects.all()
>>> <QuerySet []>
```

### 객체를 만드는 3가지 방식

- __첫번째 방법__
  - `article = Article()` :  클래스로부터 인스턴스 생성
  - `article.title` : 인스턴스로 클래스 변수에 접근해 해당 인스턴스 변수를 변경
  - `article.save()` : 인스턴스로 메소드를 호출

```python
# Article(class)로부터 article(instance) 생성!
article = Article()
article
>>> <Article: Article object (None)>

article.title = 'first' # 인스턴스 변수(title)에 값을 할당
article.content = 'django!' # 인스턴스 변수(content)에 값을 할당

# save 를 하고 확인하면 저장된 것을 확인할 수 있다
article.save()
article
>>> <Article: Article object (1)>
Article.objects.all()
>>> <QuerySet [Article: Article object (1)]>

# 인스턴스인 article을 활용하여 변수에 접근해보자(저장된걸 확인)
article.title
>>> 'first'
article.content
>>> 'django!'
article.created_at
>>> datetime.datetime(2019, 8, 21, 2, 43, 56, 49345, tzinfo=<UTC>)
```

- **두번째 방식**
  - 함수에서 keyword 인자를 넘기는 방식과 동일

```python
article = Article(title='second', content='django!!')

# 아직 저장이 안되어 있음
article
>>> <Article: Article object (None)>

# save를 해주면 저장이 된다.
article.save()
article
>>> <Article: Article object (2)>
Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```

- **세번째 방식**

  - `create()` 를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝으로 가능

```python
Article.objects.create(title='third', content='django!')
>>> <Article: Article object (3)>
```



## ◾ Read

### all()

> [참고](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#all)

- `QuerySet` return
- 리스트는 아니지만 리스트와 거의 비슷하게 동작

```python
Article.objects.all()
>>> <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
```

### get()

> [참고](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#get)

- 객체가 없으면 `DoesNotExist` 에러가 나오고 객체가 여러 개일 경우에 `MultipleObjectReturned` 오류를 띄움.
- 위와 같은 특징을 가지고 있기 때문에 unique 혹은 Not Null 특징을 가지고 있을때에만 사용할 수 있다

```python
article = Article.objects.get(pk=100)
>>> DoesNotExist: Article matching query does not exist.

Article.objects.get(content='django!')
>>> MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
**filter()**
```

### filter()

> [참고](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#filter)

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

```python
Article.objects.filter(content='django!')
>>> <QuerySet [<Article: first>, <Article: fourth>]>

Article.objects.filter(title='first')
>>> <QuerySet [<Article: first>]>
```

### The `pk` lookup shortcut

> [참고](https://docs.djangoproject.com/en/3.1/topics/db/queries/#the-pk-lookup-shortcut)

- 우리가 `.get(id=1)` 형태 뿐만 아니라 `.get(pk=1)` 로 사용할 수 있는 이유는(DB에는 id로 필드 이름이 지정 됨에도) `.get(pk=1)` 이`.get(id__exact=1)` 와 동일한 의미이기 때문이다. 

- pk는 `id__exact` 의 shortcut 이다.

```python
Blog.objects.get(id__exact=14) # Explicit form
Blog.objects.get(id=14) # __exact is implied
Blog.objects.get(pk=14) # pk implies id__exact
```



## ◾ Update

- article 인스턴스 객체 생성
- `article.title = 'byebye'` : article 인스턴스 객체의 인스턴스 변수에 접근하여 기존의 값을 `byebye` 로 변경
- `article.save()` : article 인스턴스를 활용하여 `save()` 메소드 실행

```python
# UPDATE articles SET title='byebye' WHERE id=1;
article = Article.objects.get(pk=1)
article.title
>>> 'first'

# 값을 변경하고 저장
article.title = 'byebye'
article.save()

# 정상적으로 변경된 것을 확인
article.title
>>> 'byebye'
```



## ◾ Delete

- article 인스턴스 생성후 `.delete()` 메서드 호출

```python
article = Article.objects.get(pk=1)

# 삭제
article.delete()
>>> (1, {'articles.Article': 1})

# 다시 1번 글을 찾으려고 하면 없다고 나온다.
Article.objects.get(pk=1)
>>> DoesNotExist: Article matching query does not exist.
```

































