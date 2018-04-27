from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Comment(models.Model):
    #评论人
    name = models.CharField(max_length=100)
    #评论邮箱
    email = models.EmailField(max_length=255)
    # 评论人博客地址
    url = models.URLField(blank=True)
    # 评论内容
    content = models.TextField()
    # 评论时间
    create_at = models.DateTimeField(auto_now_add=True)
    # 评论的文章
    article = models.ForeignKey('blog.Article')

    def __str__(self):
        return self.content[:20]
