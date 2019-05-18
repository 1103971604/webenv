from django.db import models

# Create your models here.

class bookinfo(models.Model):
    title=models.CharField(max_length=30,verbose_name='书名')
    bpub_date=models.DateTimeField(auto_now_add=True,verbose_name='发布日期')

    def __str__(self):
        return self.title

class heroinfo(models.Model):
    heroname=models.CharField(max_length=30,verbose_name='姓名')
    heroage=models.IntegerField(verbose_name='年龄')
    # hgender=models.BooleanField(default=True)
    hgender=models.CharField(max_length=10,choices=(('1','男'),('2','女')),verbose_name='性别')
    nbook=models.ForeignKey(bookinfo,on_delete=models.CASCADE,verbose_name='所属丛书')

    def __str__(self):
        return self.heroname




class createuser(models.Manager):
    def newuser(self,name):
        a=self.model()
        a.username=name
        a.save()


class user(models.Model):
    username=models.CharField(max_length=20)

    c=createuser()

    @classmethod
    def creat(cls,name):
        a=cls(username=name)
        a.save()
    @classmethod
    def show(cls,name):
        print(cls)  #返回是一个 类
        return cls.c.get(username=name)









