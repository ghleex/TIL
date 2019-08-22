from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')  # 이것은 DB가 바꾼 것. ORM 권장
    # articles = Article.objects.all()[::-1]  # python 이 변경한 것
    context = {'articles': articles,}

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 1. 첫 번째 방법으로 저장: 'from .models import Article' 추가 필요
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()

        # 2.
        article = Article(title=title, content=content)
        article.full_clean()    # 유효성 검증
    except: # 검증 시 오류 발생한다면
        raise ValidationError('Validation Error Occurred')
    else:
        article.save()
        return redirect(f'/articles/{article.pk}/')   # 메인 페이지로 redirect
        
        

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')    # DB를 건드리기 때문에 메인페이지로 돌리기


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')    
