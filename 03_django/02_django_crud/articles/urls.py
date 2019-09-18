from django.urls import path
from . import views

app_name = 'articles' # app_name 변수명은 고정
urlpatterns = [
    path('', views.index, name='index'),    
    path('create/', views.create, name='create'),   # NEW(GET) + CREATE(POST)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),    
    path('<int:pk>/update/', views.update, name='update'),  # EDIT(GET) + UPDATE(POST)
]
