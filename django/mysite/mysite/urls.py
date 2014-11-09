from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from django.contrib import admin
from books import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^hello/$', hello),('^time/$', current_datetime),
	(r'^another-time-page/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^meta/$', display_meta),
	(r'^search-form/$', views.search_form),
	(r'^search/$', views.search),
	

)
