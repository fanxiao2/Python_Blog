from django import template
from django.db.models.aggregates import Count
from ..models import Article, Category, Tag

register = template.Library()

# 获取数据库中前10篇文章
@register.simple_tag
def get_recent_articles(num=10):
    return Article.objects.all().order_by('-create_at')[:num]

# 归档
@register.simple_tag
def archive():
    return Article.objects.dates('create_at','month',order='DESC')

# 分类
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)

# 标签
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
