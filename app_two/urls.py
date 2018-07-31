from django.conf.urls import url
from app_two import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users$', views.users, name='users'),
    url(r'^help$', views.help, name='help'),
]