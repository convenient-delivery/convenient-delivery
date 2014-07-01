from django.conf.urls import patterns, url

from order_processor import views

urlpatterns = patterns('',
    	url(r'^$', views.index, name='index'),
      url(r'^order/', views.order, name='order')
)
