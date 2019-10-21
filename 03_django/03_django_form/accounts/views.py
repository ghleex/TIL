from IPython import embed
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login # 이름 바꾸기
from django.contrib.auth import logout as auth_logout # 이름 바꾸기
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
    # 로그인 상태에서 또 회원가입 페이지로 들어가면 안 되니까
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save() 를 통해 반환된 User 클래스의 인스턴스를 auth_login 의 인자로 전달
            user = form.save()
            auth_login(request, user)
            # 메인 페이지로 redirect
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)


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
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')
