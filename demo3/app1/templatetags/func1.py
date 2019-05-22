from django import template
from ..views import Category

register = template.Library()


@register.filter(name='low')
def low(a):
    return a.lower()



@register.simple_tag()
def categorys():
    return Category.objects.all()