from django.contrib import admin
from .models import Category,Articles,Pags,Feedback
# Register your models here.

admin.site.register(Category)
admin.site.register(Articles)
admin.site.register(Pags)
admin.site.register(Feedback)