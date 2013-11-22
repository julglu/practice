from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from library.views import BooksList, AuthorsList, BookDetail, AuthorDetail

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'pages.views.home'),
    url(r'^log/', 'pages.views.listing'),
    url(r'^library/$', BooksList.as_view()),
    url(r'^library/books/$', BooksList.as_view()),
    url(r'^library/books/(?P<pk>\d+)/$', BookDetail.as_view()),
    url(r'^library/authors/$', AuthorsList.as_view()),
    url(r'^library/authors/(?P<pk>\d+)/$', AuthorDetail.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
