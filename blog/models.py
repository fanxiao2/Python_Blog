import markdown
from django.utils.html import strip_tags
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
    # 阅读量
    reading = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title

    # 自定义get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-create_at']

    # 阅读 +1
    def increase_reading(self):
        self.reading +=1
        self.save(update_fields=['reading'])

    # 自动生成摘要
    def save(self, *args, **kwargs):
        #摘要没填写的情况下
        if not self.abstract:
            # 实例化一个markdown类,渲染内容格式
            md = markdown.Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',])
            # 将markdown渲染成html文本，然后剔除html标签，从纯文本中提取前50个字符填充给摘要
            self.abstract = strip_tags(md.convert(self.content))[:50]
        # 调用父类的save方法将数据保储存数据库中
        super(Article, self).save(*args, **kwargs)
