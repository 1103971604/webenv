from django.db import models
from app1.models import Articles
# Create your models here.

class Comment(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    tex=models.TextField(max_length=150)
    title=models.ForeignKey(Articles,on_delete=models.CASCADE)








