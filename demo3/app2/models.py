from django.db import models
from app1.models import Articles
# Create your models here.

class Comment(models.Model):
    username=models.CharField(max_length=30,verbose_name='用户名')
    email=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    url=models.URLField(blank=True,null=True,verbose_name='个人主页')
    tex=models.TextField(max_length=150,verbose_name='评论内容')
    title=models.ForeignKey(Articles,on_delete=models.CASCADE)
    creat_time=models.DateTimeField(auto_now_add=True,verbose_name='发布日期')

    def __str__(self):
        return self.username






