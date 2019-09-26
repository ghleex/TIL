from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': '제목을 입력하세요',
#             }
#         )
#     )
#     # model 과 다른 부분. TextField가 없어서 max_length 없이 씀
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': '내용을 입력하세요',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#     )

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력하세요',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력하세요',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Article
        # fields = ('title', 'content')
        fields = '__all__'            # 전체 입력 필드 관련 컬럼 다 쓰기
        # exclude = ('title')         # 'title' 제외한 나머지 필드만 쓴다

        # 1. 위젯을 meta에 넣기
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'

        #     })
        # }

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        max_length=140,
        widget=forms.TextInput(
            attrs={
                'class': 'my-comment',
                'placeholder': '댓글을 입력하세요',
            }
        )
    )
    
    class Meta:
        model = Comment
        fields = '__all__'


