from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from .views import LNMCallbackUrlApiView

urlpatterns = [
    path('lnm/', LNMCallbackUrlApiView.as_view(), name='lnm_callback_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
