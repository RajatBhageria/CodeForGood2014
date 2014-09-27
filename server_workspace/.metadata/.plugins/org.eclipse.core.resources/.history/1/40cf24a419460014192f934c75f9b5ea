from django.conf.urls import patterns, include, url

from django.contrib import admin
import views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChatServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', views.test_page),
    url(r'^message/$', views.route_message),
    url(r'^initializeData/$', views.initialize_data),
    #url(r'^message/$', 'django_twilio.views.message', {
     #   'message': 'Thanks for the SMS. Talk to you soon!',
    #}),
)
