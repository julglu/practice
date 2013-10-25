from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.home'),
    url(r'^log/', 'pages.views.listing'),
    url(r'^library/$', 'library.views.book_list'),
    url(r'^library/books/$', 'library.views.book_list'),
    url(r'^library/authors/$', 'library.views.author_list'),
    url(r'^library/authors/(?P<author_id>\d+)/$', 'library.views.author_card'),
    url(r'^library/books/(?P<book_id>\d+)/$', 'library.views.book_card'),

)
