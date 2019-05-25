
from django.conf.urls import url
from . import views
from . import  feed
app_name='app1'
urlpatterns=[
    url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^index/$',views.index,name='index'),
    url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^selcategory/(\d+)$',views.selategory,name='selcategory'),
    url(r'^seltag/(\d+)/$',views.seltag,name='seltag'),
    url(r'^rss/$',feed.App1Feed(),name='rss'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^addimg/$',views.addimg,name='addimg'),

]