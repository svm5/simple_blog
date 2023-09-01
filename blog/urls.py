from django.urls import re_path

from . import views


urlpatterns = [
    re_path('^register/$', views.register, name="register"),
    re_path('^login/$', views.LoginUser.as_view(), name="login"),
    re_path('^bloggers/(?P<pk>\d+)$', views.BlogerDetailView.as_view(), name='bloger-detail'),
    re_path('^bloggers/$', views.BlogerListView.as_view(), name='bloggers'),
    re_path('^blogs/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path('^blogs/$', views.BlogsListView.as_view(), name='blogs'),
    re_path('', views.index, name='index'),
]