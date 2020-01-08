from django.urls import path
from . import views     # 생성한 app pages 폴더 내 views.py 파일

urlpatterns = [
    # 원래 app url 은 아래쪽으로 작성
    # project url과 settings는 위로 작성
    path('index/', views.index),    
    path('introduce/<name>.<age>/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<name>/', views.hello),
    path('times/<int:num1>.<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('isitgwangbok2/', views.isitgwangbok2),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
