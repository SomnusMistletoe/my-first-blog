from django.conf.urls import url
from . import views

urlpatterns = [
    #views.post_list意味着要在view.py中创建post_list视图
    #name设置的是url的名字
    url(r'^$', views.post_list, name='post_list'),

    #(?P<pk>[0-9]+)表示将[0-9]+中的内容放入到变量pk中，这个变量可以传参到post_detail视图中
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]