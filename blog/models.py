from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # 引入reverse函数
from django.utils.six import python_2_unicode_compatible
# Create your models here.

# 分类
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# 标签
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# 文章
@python_2_unicode_compatible
class Article(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 内容
    content = models.TextField()
    # 摘要
    abstract = models.CharField(max_length=200, blank=True)
    # 所属分类
    category = models.ForeignKey(Category)
    # 标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 发布人（作者）
    author = models.ForeignKey(User)
    # 发布时间（创建时间）
    create_at = models.DateField()
    # 更新时间（修改时间）
    update_at = models.DateField()

    def __str__(self):
        return self.title

    # 自定义get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})
