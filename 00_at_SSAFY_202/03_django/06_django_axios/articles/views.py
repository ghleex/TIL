import hashlib
from IPython import embed
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    # session 에 visits_number(방문 횟수) 키로 접근하여 값 가져오기
    # 기본적으로 존재하지 않는 키이므로, 키가 없다면(방문한 적이 없다면) 0 값을 가져오도록 해야 함
    visits_num = request.session.get('visits_num', 0)

    # 그리고 가져온 값을 session 의 visits_num 에 매 번 1 씩 증가한 값으로 할당
    # 값을 늘리는 이유: 유저가 방문한 횟수 확인
    request.session['visits_num'] = visits_num + 1
    # session data 내의 새로운 정보를 수정했을 때 django 는 수정한 것을 알지 못하므로
    # 아래와 같이 설정
    request.session.modified = True

    articles = Article.objects.all()
    # articles = get_list_or_404(Article)   # 적절한 장소에서 쓰자
    context = {'articles': articles, 'visits_num': visits_num,}
    
    return render(request, 'articles/index.html', context)
    

@login_required
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
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # hashtag
            for word in article.content.split():    # 공백 기준으로 content 를 list 로 쪼개기
                if word.startswith('#'):    # '#' 으로 시작하는 요소만 선택
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # word 와 같은 hashtag 를 찾아, 이미 존재한다면 기존 객체(.get)를 가져오고 없으면 새로운 객체 생성(.create)
                    article.hashtags.add(hashtag)
                    # created 를 사용하지 않는 경우, hashtag[0] 과 같이 작성
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
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    c_form = CommentForm()        # 댓글 출력 위한 폼 출력
    context = {
        'article': article,
        'c_form': c_form,
        'comments': comments,
        'person': person,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
        # if request.method == 'POST':
            article.delete()
        else:
            return redirect(article)
            # return redirect('articles:detail', article_pk)
    return redirect('articles:index')
    # else:
    #     return redirect(article)


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:    # 새로 추가된 부분: 작성자와 로그인 사용자가 동일인물인지 확인
        if request.method == 'POST':
            # form = ArticleForm(request.POST)
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                # article.save()
                article = form.save()
                article.save()
                # hashtag
                article.hashtags.clear()     # 해당 article 의 hashtag 를 모두 지우는 과정
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect(article)
        else:
            # ArticleForm 을 초기화: 이전에 DB에 저장된 데이터를 넣어준 상태
            # form = ArticleForm(initial={'title': article.title, 'content': article.content})
            # __dict__ :  article 객체 데이터를 딕셔너리 자료형으로 변환
            # 아래와 같이 짧게 쓸 수 있다. python 과 django 가 섞인 것
            # form = ArticleForm(initial=article.__dict__)
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    # 1. POST 방식일 때 오는 FORM: 검증에 실패한 form - 오류메시지도 포함된 상태
    # 2. GET 방식일 때 오는 FORM: 초기화된 form
    context = {'form': form, 'article':article,}
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        # if request.method == 'POST':          # decorator 있어서 필요 없음
        c_form = CommentForm(request.POST)    # binding 작업: 폼에 데이터 넣기
        if c_form.is_valid():
            # 객체를 Create 하지만, db 에 레코드는 작성하지 않음
            comment = c_form.save(commit=False)            
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
    return redirect('articles:detail', article_pk)
    

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        # if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are not authroized. 401 ERROR', status=401)
    

@login_required
def like(request, article_pk):
    if request.is_ajax():
        article = get_object_or_404(Article, pk=article_pk)
        # 해당 게시글에 '좋아요'를 누른 사람 중 현재 접속 user 가 있다면 '좋아요' 취소도 가능해야 함
        if article.like_users.filter(pk=request.user.pk).exists():
            # get 을 쓰면 키가 없는 경우 오류가 나므로 filter 사용
            article.like_users.remove(request.user)
            liked = False
            
        # if request.user in article.like_users.all():
        #     article.like_users.remove(request.user)
            # '좋아요' 취소
        else:
            article.like_users.add(request.user)
            liked = True
            # '좋아요' 클릭
        # return redirect('articles:index')
        context = {'liked': liked, 'count': article.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()


@login_required
def follow(request, article_pk, user_pk):
    # person: 게시글 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # user: 접속 유저
    user = request.user
    if person != user:  # 자기 자신한테 follow 할 수 없도록
        # 내(request.user)가 게시글 유저(person) 팔로워 목록에 이미 존재한다면,
        # if user in person.followers.all():
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('articles:detail', article_pk)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag': hashtag, 'articles': articles,}
    return render(request, 'articles/hashtag.html', context)
