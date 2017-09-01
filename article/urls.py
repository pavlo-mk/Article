from django.conf.urls import url, include
import article

from . import views




urlpatterns = [
    url(r'^test/1/', views.article_one),
    url(r'^test/2/', views.article_two),
    url(r'^articles/all/$', views.articles),
    url(r'^articles/get/(?P<id>\d)/$', views.article),  #(?P<id>[1-9])
]