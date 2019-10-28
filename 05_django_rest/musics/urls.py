from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="This is a Music info API service.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="test@ssafy.com"),
      license=openapi.License(name="SSAFY License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('musics', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),
    path('artists/', views.artist_list),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
