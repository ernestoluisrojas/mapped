from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapped_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mapped_app.views.home', name='home'),
    url(r'^open$', 'mapped_app.views.open', name='open'),
    url(r'^leaf$', 'mapped_app.views.leaf', name='leaf'),
    url(r'^openlayer$', 'mapped_app.views.openlayer', name='openlayer'),
)



#for development
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )