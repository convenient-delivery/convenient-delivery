from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('registration.backends.default.urls')),
  url(r'^/*', include('order_processor.urls', namespace="order_processor")), 
=======
  url(r'^polls/', include('polls.urls', namespace="polls")),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('registration.backends.default.urls')),
  url(r'^/*', include('order_processor.urls')), 
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
)
