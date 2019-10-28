from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from .models import Music, Artist, Comment

# Create your views here.
@api_view()
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    # 다중객체를 가져온다면 `many=True` 속성 추가
    # music 라는 QuerySet 을 json type 으로 바꾸어 줌
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, music_pk):
    serializer = CommentSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comment_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated'})
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted'})
