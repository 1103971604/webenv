from django.conf.urls import url
from . import views

app_name='booktest'

urlpatterns = [
    url(r'^list/$',views.list,name='list'),
    url(r'^detil/(\d+)/$',views.detil,name='detil'),
    url(r'^index/$',views.index,name='index'),
    url(r'^delbook/(\d+)/$',views.delbook,name='delbook'),
    url(r'^deldetil/(\d+)/$',views.deldetil,name='deldetil'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^adddetil/(\d+)/$',views.adddetil,name='adddetil'),
    url(r'^setbook/(\d+)$',views.setbook,name='setbook'),
    url(r'^setdetil/(\d+)/$',views.setdetil,name='setdetil'),


]