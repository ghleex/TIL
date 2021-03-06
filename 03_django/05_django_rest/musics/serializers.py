from rest_framework import serializers
from .models import Music, Artist

class MusicSerializer(serializers.ModelSerializer):
    class Meta(Music):
        model = Music
        fields = ('id', 'title', 'artist_id',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta(Artist):
        model = Artist
        fields = ('id', 'name',)
