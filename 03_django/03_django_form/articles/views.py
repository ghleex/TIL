from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    # articles = get_list_or_404(Article)   # 적절한 장소에서 쓰자
    context = {'articles': articles,}
    
    return render(request, 'articles/index.html', context)
    

def create(request):
    if request.method == 'POST':
        # form 인스턴스 생성 후 요청 받은 데이터를 통째로 인자로 받는다.
        # 아래 과정은 binding 으로 불리며, 유효성 검사가 가능하도록 만들어준다.
        form = ArticleForm(request.POST)
        # form 의 유효성 검사
        if form.is_valid():
            # form.cleaned_data 로 정제된 데이터를 받음
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)  # 위에서 유효성 검사가 끝났으므로 save할 필요 없이 사용 가능
            article = form.save()
            return redirect(article)

    else:   # GET 방식
        form = ArticleForm()
    # 상황에 따라 CONTEXT 에 넘어가는 두 가지 form
    # 1. GET 방식: 기본 FORM
    # 2. POST 방식: 검증에 실패했을 때의 form (is_valid() == False)

    # 아래 두 줄은 안쪽으로 넣으면 POST 에서 튕겨 나왔을 때 갈 곳이 없음
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()        # article의 모든 댓글
    c_form = CommentForm()        # 댓글 출력 위한 폼 출력
    context = {'article': article, 'c_form': c_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect(article)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # form = ArticleForm(request.POST)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            article = form.save()
            return redirect(article)
    else:
        # ArticleForm 을 초기화: 이전에 DB에 저장된 데이터를 넣어준 상태
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        # __dict__ :  article 객체 데이터를 딕셔너리 자료형으로 변환
        # 아래와 같이 짧게 쓸 수 있다. python 과 django 가 섞인 것
        # form = ArticleForm(initial=article.__dict__)
        form = ArticleForm(instance=article)
    
    # 1. POST 방식일 때 오는 FORM: 검증에 실패한 form - 오류메시지도 포함된 상태
    # 2. GET 방식일 때 오는 FORM: 초기화된 form
    context = {'form': form, 'article':article,}
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    # if request.method == 'POST':          # decorator 있어서 필요 없음
    c_form = CommentForm(request.POST)    # binding 작업: 폼에 데이터 넣기
    if c_form.is_valid():
        # 객체를 Create 하지만, db 에 레코드는 작성하지 않음
        comment = c_form.save(commit=False)            
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)
    

@require_POST
def comments_delete(request, article_pk, comment_pk):    
    # if request.method == 'POST':
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    
