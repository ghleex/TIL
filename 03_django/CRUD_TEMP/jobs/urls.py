from django.urls import path
from . import views

app_name = 'jobs' # app_name 변수명은 고정
urlpatterns = [
    path('', views.index, name='index'),
    path('past_life/', views.past_life, name='past_life'),
]
