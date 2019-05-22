
from django.conf.urls import url
from . import views
app_name='app1'
urlpatterns=[
    url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^index/$',views.index,name='index'),
    url(r'^single/(\d+)/$',views.single,name='single')
]