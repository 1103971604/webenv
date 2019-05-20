from django.contrib import admin
from .models import list,listcount,AreaInfo,UserInfo
# Register your models here.

class liststyle(admin.ModelAdmin):
    list_display = ['title']

class listnumstyle(admin.ModelAdmin):
    list_display = ['choice','num','list']

class Userstyle(admin.ModelAdmin):
    list_display = ['username','pwd','sign']

admin.site.register(list,liststyle)

admin.site.register(listcount,listnumstyle)

admin.site.register(UserInfo,Userstyle)

admin.site.register(AreaInfo)





