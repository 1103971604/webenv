from django.contrib import admin
from .models import list,listcount
# Register your models here.

class liststyle(admin.ModelAdmin):
    list_display = ['title']

class listnumstyle(admin.ModelAdmin):
    list_display = ['choice','num','list']

admin.site.register(list,liststyle)
admin.site.register(listcount,listnumstyle)






