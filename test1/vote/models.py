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
