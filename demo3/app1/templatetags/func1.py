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
def Messiges(id):
    article=Articles.objects.get(pk=id)
    return article.comment_set.all()