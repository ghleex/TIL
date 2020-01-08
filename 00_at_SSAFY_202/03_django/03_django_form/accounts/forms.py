from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()    # this returns 'User'
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()    # 현재 project 의 active user 를 model 로 사용
        # 따라서 위와 같이 설정함으로써 accounts.User 를 가리키게 됨
        fields = UserCreationForm.Meta.fields + ('email',)
