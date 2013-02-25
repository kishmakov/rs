from django.conf.urls import patterns
from app.views import process_beg, process_go
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   ('^$', process_beg),
   ('^go/$', process_go),
   (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
