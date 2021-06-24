from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm
import datetime
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests

def index(request,unitNo ,param):

    dt_now = datetime.datetime.now()
    print(request)
    article = Article(content=param,user_name=unitNo,day_now=str(datetime.date.today()),time_now=str(dt_now.hour)+"時"+str(dt_now.minute)+"分"+str(dt_now.second)+"秒"
    ,time_hours=dt_now.hour,time_minutes=dt_now.minute,time_seconds=dt_now.second)
    article.save()
    
    response = requests.get(
    'http://******/bbs/post/'+str(unitNo)+"/"+str(param))

    print('http://******/bbs/post/'+str(unitNo)+"/"+str(param))
    return HttpResponse("UnitNo."+str(unitNo)+",value."+str(param)+"cm")

