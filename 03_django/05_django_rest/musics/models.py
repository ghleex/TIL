from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Music(models.Model):
    # serializer 에서 music_set 이름을 바꿔버리려고 함
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
