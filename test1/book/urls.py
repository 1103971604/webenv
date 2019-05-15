from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$',views.list),
    url(r'^detil/(\d+)/$',views.detil),
    url(r'^index/$',views.index)
]