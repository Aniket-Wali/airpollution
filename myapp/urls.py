from django.conf.urls import url, include

from myapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/',views.index,name='home'),
    url(r'^search/', views.SearchPage.as_view(),name='Search'),
    url(r'^Result/', views.SearchResult.as_view(),name='result'),
]