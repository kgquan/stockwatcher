from django.urls import path
from stocks import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #path('<string:symbol>/', views.detail, name='detail'),
    path('stocks/<symbol>/', views.detail, name='detail'),
]