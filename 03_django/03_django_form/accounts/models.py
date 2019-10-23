from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):   # 그냥 User 는 빈 껍데기
    # django 는 맞춤 모델을 참조하는 AUTH_USER_MODEL 설정 값을 제공하므로
    # 기본 User model 을 override 하도록 만들 수 있음
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
