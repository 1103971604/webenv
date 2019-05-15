from django.contrib import admin
from .models import bookinfo,heroinfo
# Register your models here.

class bookinfoAdmin(admin.ModelAdmin):
    list_display = ['title','bpub_date']
    list_filter = ['title','bpub_date']

class heroinfoAdmin(admin.ModelAdmin):
    list_display = ['heroname','hgender','nbook']
    list_filter = ['hgender']

admin.site.register(bookinfo,bookinfoAdmin)
admin.site.register(heroinfo,heroinfoAdmin)







