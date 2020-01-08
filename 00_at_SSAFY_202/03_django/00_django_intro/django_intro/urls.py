"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include는 옮긴 pages의 url을 보기 위하여..


# url 경로 마지막에 / 붙이기
# path('hello/<str:name>/', views.hello) 역시 가능
urlpatterns = [
    # 앞으로는 App 1개 당 한 줄만 쓸 것임
    path('utilities/', include('utilities.urls')), # utilities app의 url을 연결하기 위한 것
    path('pages/', include('pages.urls')),  # pages app의 url을 보기 위한 것
    path('admin/', admin.site.urls),
]
