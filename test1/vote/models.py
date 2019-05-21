from django.db import models

# Create your models here.
class list(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')

    def __str__(self):
        return self.title

class listcount(models.Model):
    choice=models.CharField(max_length=20,verbose_name='选项')
    num=models.IntegerField(verbose_name='票数')
    list=models.ForeignKey(list,on_delete=models.CASCADE,verbose_name='标题')

    def __str__(self):
        return self.choice

class AreaInfo(models.Model):
    diqu=models.CharField(max_length=30,verbose_name='地区')
    bianhao=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.diqu


class UserInfo(models.Model):
    # unique 值不能重复
    username=models.CharField(max_length=16,verbose_name='用户名')
    pwd=models.CharField(max_length=16,verbose_name='密码')
    sign=models.CharField(max_length=10,choices=(('1','用户'),('2','管理员')),default=1,verbose_name='标识',null=True,blank=True)

    def __str__(self):
        return self.username

