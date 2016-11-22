from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/', views.index, name='index'),
    url(r'^(\d+)', views.detail, name='detail'),
    url(r'^$', views.home, name='home'),

]