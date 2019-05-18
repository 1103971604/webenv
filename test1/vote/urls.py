from django.conf.urls import url
from .views import *

app_name='votetest'

urlpatterns=[
    url(r'^index/$',index,name='index'),
    url(r'^choice/(\d+)/$',choice,name='choice'),
    url(r'^listcountA/(\d+)/$',listcountA,name='listcountA'),



]