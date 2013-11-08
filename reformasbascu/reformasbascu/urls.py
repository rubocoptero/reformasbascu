from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'render.views.home', name='home'),
    url(r'^gallery', 'render.views.gallery', name='gallery'),
    url(r'^robots\.txt$', 
        TemplateView.as_view(
            template_name='robots.txt', 
            content_type='text/plain'
        )
    ),
    url(r'^humans\.txt$', 
        TemplateView.as_view(
            template_name='humans.txt', 
            content_type='text/plain'
        )
    ),
    url(r'^sitemap\.xml$', 
        TemplateView.as_view(
            template_name='sitemap.xml', 
            content_type='application/xml'
        )
    ),
    # Examples:
    # url(r'^$', 'reformasbascu.views.home', name='home'),
    # url(r'^reformasbascu/', include('reformasbascu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
