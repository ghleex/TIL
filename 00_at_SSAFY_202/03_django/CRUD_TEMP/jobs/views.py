import requests
from pprint import pprint
from faker import Faker
from decouple import config
from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')


def past_life(request):
    # 이름 데이터 받기    
    name = request.POST.get('name')
    
    # DB 에 matching 되는 name 가져오기
    # .get() 은 간단하지만 해당 값이 없을 때 오류가 남
    # filter 는 무조건 query_set으로 가져옴(리스트 형태) / error를 내지 않음
    person = Job.objects.filter(name=name).first()
    # DB 에 person이 있는지 없는지 판단
    if person:  # DB 에서 찾은 경우
        past_job = person.past_job               

    else:       # DB 에서 못 찾은 경우 / person이 빈 query set(==False)
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job)  # 새로운 레코드 추가
        person.save()

    # GIPHY (past_job 을  API 에 요청을 보내 응답 받음)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1&rating=R'
    data = requests.get(url).json()
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    # json 타고 들어갈 때 리스트 있는지 확인하기!
    except IndexError:
        image = None
    
    context = {'person': person, 'image': image, }
    return render(request, 'jobs/past_life.html', context)