from django.conf.urls import url
from .views import *

app_name='votetest'

urlpatterns=[

    url(r'^index/$',index,name='index'),
    url(r'^choice/(\d+)/$',choice,name='choice'),
    url(r'^listcountA/(\d+)/$',listcountA,name='listcountA'),
    url(r'^loginout/$',loginout,name='loginout'),
    url(r'^login/$', Login, name='login'),
    url(r'^register/$',Register,name='register'),
]






