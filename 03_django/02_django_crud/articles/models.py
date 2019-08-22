from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)     # 기본값: blank=False
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # 객체표현
        return self.title   # 보통 첫 번째 컬럼 출력