from django.conf.urls.defaults import *
from django.conf import settings

import os.path
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #Main Pages
    #(r'^admin_tools/', include('admin_tools.urls')),
    #(r'^tinymce/', include('tinymce.urls')),
    #(r'^admin/filebrowser/', include('filebrowser.urls')),
    #(r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),



)

