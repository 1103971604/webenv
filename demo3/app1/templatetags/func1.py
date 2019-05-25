from django import template
from ..models import Category,Articles,Pags,absimg
register = template.Library()


@register.filter(name='low')
def low(a):
    return a.lower()

# 筛选器
@register.filter()
def txtlen(val,num):
    return val[:num]
# 标签
@register.simple_tag()
def categorys():
    return Category.objects.all()


@register.simple_tag()
def getnewcomments(num):
    return Articles.objects.all().order_by('-create_time')[:num]


@register.simple_tag()
def getcategorys():
    return Category.objects.all()


@register.simple_tag()
def gettags():
    return Pags.objects.all()


# 查询所有图片标签
@register.simple_tag()
def getimgs():
    return absimg.objects.all()