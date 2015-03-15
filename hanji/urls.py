from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

   url(r'^admin/', include(admin.site.urls)),



   url(r'^accounts/login/$', 'signup.views.login'),
   url(r'^accounts/auth/$', 'signup.views.auth_view'),
   url(r'^accounts/logout/$','signup.views.logout'),
   url(r'^accounts/loggedin/$', 'signup.views.loggedin'),
   url(r'^accounts/invalid/$', 'signup.views.invalid_login'),


)

