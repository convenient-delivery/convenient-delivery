from django.conf.urls import patterns, url

from order_processor import views

urlpatterns = patterns('',
    	url(r'^$', views.index, name='index'),
      url(r'^order/', views.order, name='order'),
      url(r'^driver/', views.driver, name='driver'),
      url(r'^signup/', views.signup, name='signup'),
      url(r'^successfulsignup/', views.successfulsignup, name='successfulsignup'),
)
