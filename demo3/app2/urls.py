from django.conf.urls import url
from . import views
app_name='app2'
urlpatterns=[
    url(r'^msg/(\d+)/$',views.Msg,name='msg'),
]