from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import JSONWebTokenAuthentication
from django.shortcuts import render
from .serializers import TodoSerializer

# Create your views here.
@api_view(['POST'])
# 아래 두 가지 decorator 는 settings.py 에서 이미 default 로 설정해둔 것이므로 주석 처리
# # 1. 인증 받은 사용자만 허가(로그인 여부만 체크)
# @permission_classes((IsAuthenticated, ))    # tuple 로 넣어주어야 함
# # 2. jwt 인증
# @authentication_classes((JSONWebTokenAuthentication, ))    # tuple 로 넣어주어야 함
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request):
    pass
