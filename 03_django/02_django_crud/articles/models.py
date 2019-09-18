from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)     # 기본값: blank=False
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # 객체표현
        return self.title   # 보통 첫 번째 컬럼 출력

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk])     # return 값: articles/10/
        return reverse('articles:detail', kwargs={'pk': self.pk})   # articles/10/
        # 주의사항
        # reverse 함수에 args 와 kwargs 를 동시에 인자로 보낼 수 없음!
        # 둘 중 하나만 사용해야 함!
