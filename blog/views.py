from django.shortcuts import render
from django.http import HttpResponse # 导入HttpResponse函数
from .models import Article
# Create your views here.

def index(request):
    article_list = Article.objects.all().order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})
