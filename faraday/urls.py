from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^turnstile/', include('turnstile.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# N.B., the 'static' function adds a URL conf that serves MEDIA files when DEBUG is
# true. When it's falsse, 'static' returns an empty list.
