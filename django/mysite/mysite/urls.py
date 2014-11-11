from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    (r'^hello/$', 'hello'),('^time/$', 'current_datetime'),
	(r'^another-time-page/$', 'current_datetime'),
	(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
	(r'^meta/$', 'display_meta'),
)

urlpatterns += patterns('books.views',
	(r'^search-form/$', 'search_form'),
	(r'^search/$', 'search'),
)

urlpatterns += patterns('contact.views',
	(r'^contact/$', 'contact'),
	(r'^contact/thanks/','thanks'),
)	
	
