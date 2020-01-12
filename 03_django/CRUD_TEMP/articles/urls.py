from django.urls import path
from . import views

app_name = 'articles' # app_name 변수명은 고정
urlpatterns = [
    path('', views.index, name='index'),    
    path('create/', views.create, name='create'),   # NEW(GET) + CREATE(POST)
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),    
    path('<int:article_pk>/update/', views.update, name='update'),  # EDIT(GET) + UPDATE(POST)
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),  # DETAIL(GET) + CREATE(POST)
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'), 
]
