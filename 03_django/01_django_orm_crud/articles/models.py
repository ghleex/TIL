from django.db import models

# Create your models here.
class Article(models.Model):    # models.Model 에서 상속 받음
    # id = models.AutoField(primary_key=True) # 자동으로 입력되도록 설정
    # id(primary key)는 기본적으로 처음 생성 시 자동으로 만들어짐
    title = models.CharField(max_length=10) # 클래스 변수: DB의 필드    
    content = models.TextField()    # 클래스 변수: DB의 필드
    created_at = models.DateTimeField(auto_now_add=True)    # 클래스 변수: DB의 필드
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번 글 - {self.title}: {self.content}'


