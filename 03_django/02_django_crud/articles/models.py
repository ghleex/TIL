from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models

# 이미지 업로드 경로 커스터마이징
def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)     # 기본값: blank=False
    content = models.TextField()
    # image = models.ImageField(blank=True)   # 굳이 올리지 않아도 저장됨 / 이미지 추가 없이도 게시글 올라갈 것임
    # image_thumbnail = ImageSpecField(
    #     source='image',     # 원본 ImageField 이름
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )    
    image = ProcessedImageField(
        # ProcessedImageField 필드의 인자로 들어가 있는 값들은
        # migrations 이후 추가되거나 수정되더라도
        # makemigrations 하지 않아도 됨
        processors=[Thumbnail(200, 300)],   # 처리할 작업 목록 / 리스트 형태
        format='JPEG',              # 저장 포맷
        options={'quality': 90},    # 추가 옵션 / 딕셔너리 형태
        upload_to='articles/images',    # media 폴더 이후 실제 저장할 경로 추가 지정(MEDIA_ROOT/article/images)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # 객체표현
        return self.title   # 보통 첫 번째 컬럼 출력

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk])     # return 값: articles/10/
        return reverse('articles:detail', kwargs={'article_pk': self.pk})   # articles/10/
        # 주의사항
        # reverse 함수에 args 와 kwargs 를 동시에 인자로 보낼 수 없음!
        # 둘 중 하나만 사용해야 함!


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'

