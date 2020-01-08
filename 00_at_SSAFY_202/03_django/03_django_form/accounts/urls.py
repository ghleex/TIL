from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # 'password/' 는 기본 제공 주소
    path('<username>/', views.profile, name='profile'), 
    # 문자열로 처리된 주소들은 모든 조건을 포함하므로 마지막에 판단하도록 최하단에 내려주어야 함
    # django 는 위에서 아래로 주소를 읽어나간다
]
