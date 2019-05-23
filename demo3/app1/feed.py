from django.contrib.syndication.views import Feed
from .models import Articles
from django.shortcuts import reverse

class App1Feed(Feed):
    title='个人博客'
    description='一个学习网站'
    link='/'

    def items(self):
        return Articles.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.bodytxt[:30]

    def item_link(self, item):
        return reverse('app1:single',args=(item.id,))