import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # 导入HttpResponse函数
from comments.forms import CommentForm #导入评论
from .models import Article, Category
# Create your views here.

def index(request):
    article_list = Article.objects.all().order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})

# 实现detail 视图

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # 阅读量 +1
    article.increase_reading()
    article.content = markdown.markdown(article.content,
                                        extensions = [
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    form = CommentForm()
    # 获取文章下对应的全部评论
    comment_list = article.comment_set.all()
    # 将文章，表单和文章下面的评论列表当做模板传递给 detail.html 模板并渲染相对应的数据
    context = {'article':article, 'form':form, 'comment_list':comment_list}
    return render(request, 'blog/detail.html', context=context)

# 归档
def archives(request, year, month):
    article_list = Article.objects.filter(create_at__year=year,create_at__month=month).order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})
# 分类
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-create_at')
    return render(request, 'blog/index.html', context={'article_list':article_list})
