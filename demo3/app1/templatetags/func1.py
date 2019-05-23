from django import template
from ..views import Category,Articles

register = template.Library()


@register.filter(name='low')
def low(a):
    return a.lower()



@register.simple_tag()
def categorys():
    return Category.objects.all()


@register.simple_tag()
def getnewcomments(num):
    return Articles.objects.all().order_by('-create_time')[:num]


@register.simple_tag()
def getcategorys():
    return Category.objects.all()
