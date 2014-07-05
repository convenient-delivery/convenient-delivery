from django.conf.urls import patterns, url

from order_processor import views

urlpatterns = patterns('',
    	url(r'^$', views.index, name='index'),
      url(r'^order/', views.order, name='order'),
      url(r'^login/', views.login, name='login'),
      url(r'^logout/', views.logout, name = 'logout'),
      url(r'^signup/', views.signup, name='signup'),
      url(r'^successfulsignup/', views.successfulsignup, name='successfulsignup'),
      url(r'^successfullogin/', views.successfullogin, name='successfullogin'),
<<<<<<< HEAD
#      url(r'^driver/', views.driver, name='driver'),
=======
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
)
