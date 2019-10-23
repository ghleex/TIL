from IPython import embed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login # 이름 바꾸기
from django.contrib.auth import logout as auth_logout # 이름 바꾸기
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def signup(request):
    # 로그인 상태에서 또 회원가입 페이지로 들어가면 안 되니까
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save() 를 통해 반환된 User 클래스의 인스턴스를 auth_login 의 인자로 전달
            user = form.save()
            auth_login(request, user)
            # 메인 페이지로 redirect
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    # 로그인 상태에서 또 로그인 페이지로 들어가면 안 되니까
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 위의 form 은 다른 form 과 다른 인자를 갖는 점에 주의!
        # 여기서는 form.get_user() 해도 값이 안 나옴
        if form.is_valid(): # 유효성 검사
            # 여기를 통과해야 form.get_user() 정보가 나온다
            # session 만들기
            auth_login(request, form.get_user())
            # login() 그대로 사용하면 view 함수 이름과 겹쳐서 바꿈
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    articles = person.article_set.all()
    comments = person.article_set.all()
    context = {'person': person, 'articles': articles, 'comments': comments,}
    return render(request, 'accounts/profile.html', context)
