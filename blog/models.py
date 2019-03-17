from django.db import models


class Blog(models.Model):
    # id(primary key)
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.CharField(max_length=20, default='codingkai', verbose_name='作者')
    body = models.TextField(verbose_name='正文')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')
    read_nums = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    category = models.ManyToManyField('Category', related_name='category', verbose_name='标签')
    is_public = models.BooleanField(default=True, verbose_name='是否公开')

    class Meta:
        verbose_name, verbose_name_plural = ('博客', '博客')

    def __str__(self):
        return self.title

    @staticmethod
    def get_all():
        return Blog.objects.filter(is_public=True)


class Category(models.Model):
    # id(primary key)
    name = models.CharField(max_length=50, verbose_name='标签名')

    class Meta:
        verbose_name, verbose_name_plural = ('标签', '标签')

    def __str__(self):
        return self.name


