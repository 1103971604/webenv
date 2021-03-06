from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


# 文章类别
class Category(models.Model):
    title=models.CharField(max_length=30,verbose_name='类别')
    class Meta():
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文章标签
class Pags(models.Model):
    title=models.CharField(max_length=30,verbose_name='标签')
    class Meta():
        verbose_name = "标签"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title


# 文章
class Articles(models.Model):
    title=models.CharField(max_length=30,verbose_name='标题')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time=models.DateTimeField(auto_now=True,verbose_name='修改时间')
    Readnum=models.PositiveIntegerField(default=0,verbose_name='阅读数')
    bodytxt=models.TextField(max_length=500,default='',verbose_name='正文')
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='文章类别')
    pag=models.ManyToManyField(Pags,verbose_name='标签')
    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name



    def __str__(self):
        return self.title


class Feedback(models.Model):
    username=models.CharField(max_length=20,verbose_name='用户名')
    emal=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    subject=models.CharField(max_length=30,verbose_name='主题')
    txt=HTMLField()

    def __str__(self):
        return self.username

class absimg(models.Model):
    img=models.ImageField(upload_to='abs',verbose_name='图片文件')
    msg=models.CharField(max_length=20,verbose_name='消息')
    class Meta():
        verbose_name = "轮播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.msg









