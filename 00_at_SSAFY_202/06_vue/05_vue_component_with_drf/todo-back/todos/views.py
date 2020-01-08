from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import JSONWebTokenAuthentication
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from .models import Todo

User = get_user_model()

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
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204: No Content; 해당 콘텐츠가 없음(삭제로 인하여 해당 데이터가 존재하지 않음을 알려주기 위한 용도)
        return Response(status=204)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        # print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료됐습니다.'})


@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        return HttpResponseForbidden()
        # return Response(status=403)
    serializer = UserSerializer(user)
    return Response(serializer.data)
