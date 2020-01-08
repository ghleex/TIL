from django.contrib import admin
from .models import Article, Comment, Hashtag

# Register your models here.
# admin에 등록하는 코드는 두 가지 스타일이 있다
@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at', 'user_id',)

admin.site.register(Article, ArticleAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id', 'user_id',)
