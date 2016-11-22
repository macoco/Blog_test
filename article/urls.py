from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/', views.index, name='index'),
    #url(r'^$', views.detail, name='detail'),
    url(r'^$', views.home, name='home'),

]