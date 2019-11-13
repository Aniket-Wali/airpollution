from django.conf.urls import url, include

from myapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/',views.index,name='home'),
]