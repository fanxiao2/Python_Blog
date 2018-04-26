import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # 导入HttpResponse函数
from .models import Article, Category
# Create your views here.

def index(request):
    article_list = Article.objects.all().order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})

# 实现detail 视图

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown.markdown(article.content,
                                        extensions = [
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    return render(request, 'blog/detail.html', context={'article':article})

# 归档
def archives(request, year, month):
    article_list = Article.objects.filter(create_at__year=year,create_at__month=month).order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})
# 分类
def category(request, pk):
    cate = get_object_or_404(Category, pk)
    article_list = Article.objects.filter(category=cate).order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})
