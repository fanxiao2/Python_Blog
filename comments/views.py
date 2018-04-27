from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .models import Comment
from .forms import CommentForm

# Create your views here.
def article_comment(request, article_pk):
    # 使用get_object_or_404 获取文章，当文章存在是返回，不存在返回404页面
    article = get_object_or_404(Article, pk=article_pk)
    # post表单处理
    if request.method == 'POST':
        #构造CommentForm实例
        form = CommentForm(request.POST)
        #坚持表单中数据格式是否符合要求
        if form.is_valid():
            # 检查数据库是否合法，合法则保存 commit=False是先生成comment模型类的实例，但先不保存到数据库中
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.article = article
            # 保存评论内容
            comment.save()
            # 重定向返回url
            return redirect(article)
        else:
            # 检查数据库如果不合法的话需要重新渲染详情页，并且渲染表单错误
            comment_list = article.comment_set.all()
            context = {'article':article, 'form':form, 'comment_list':comment_list}
            return render(request, 'blog/detail.html', context=context)
    return redirect(article)
