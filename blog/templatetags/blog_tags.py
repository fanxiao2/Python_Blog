from django import template
from ..models import Article, Category

register = template.Library()

# 获取数据库中前3篇文章
@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-create_at')[:num]

# 归档
@register.simple_tag
def archive():
    return Article.objects.dates('create_at','month',order='DESC')

# 分类
@register.simple_tag
def get_categories():
    return Category.objects.all()
