import hashlib
from django import template

register = template.Library()
# 기존 템플릿 라이브러리에
# 아래 함수를 추가함
@register.filter
def makemd5(email):
    return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()