from django.db import models

# Create your models here.

class bookinfo(models.Model):
    title=models.CharField(max_length=30)
    bpub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class heroinfo(models.Model):
    heroname=models.CharField(max_length=30)
    heroage=models.IntegerField(max_length=5)
    hgender=models.BooleanField(default=True)
    nbook=models.ForeignKey(bookinfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.heroname


