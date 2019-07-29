from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 分类表
class Category(models.Model):
    """
        Django 要求模型必须继承 models.Model 类。
        Category 只需要一个简单的分类名 name 就可以了。
        CharField 指定了分类名 name 的数据类型，CharField 是字符型，
        CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
        当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
        """
    name = models.CharField(max_length=100)


# 标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)


# 文章表
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET('未分类'))
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
