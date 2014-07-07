from django.conf.urls import patterns, url

from order_processor import views

urlpatterns = patterns('',
    	url(r'^$', views.index, name='index'),
      url(r'^login/', views.login, name='login'),
      url(r'^logout/', views.logout, name = 'logout'),
      url(r'^signup/', views.signup, name='signup'),
      url(r'^successfulsignup/', views.successfulsignup, name='successfulsignup'),
      url(r'^successfullogin/', views.successfullogin, name='successfullogin'),
      url(r'^driver/', views.driver, name='driver'),
      url(r'^order_details/(?P<order_id>\d+)/$', views.order_details, name = 'order_details'),
      url(r'^new_order/', views.new_order, name = 'new_order'),
)
