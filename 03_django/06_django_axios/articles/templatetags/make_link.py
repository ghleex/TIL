from django import template

register = template.Library()


@register.filter
def hashtag_link(word):
    # article 객체가 들어갈 word 에는
    # article 의 content 만 모두 가져와
    # 이중 hashtag 에만 링크를 붙일 것임
    content = word.content + ' '
    hashtags = word.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(hashtag.content+' ', f'<a href="/articles/{hashtag.pk}/hashtag">{hashtag.content}</a> ') # 마지막 공백이 있음에 주의!
        # html a 태그를 씌운 hashtag.content 로 바꿔줄 것임
    return content
