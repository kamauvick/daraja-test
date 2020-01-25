from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from .views import LNMCallbackUrlApiView, C2BConfirmationApiView, C2BValidationApiView

urlpatterns = [
    path('lnm/', LNMCallbackUrlApiView.as_view(), name='lnm_callback_url'),
    path('validation_url/', C2BValidationApiView.as_view(), name='c2b_validation_url'),
    path('confirmation_url/', C2BConfirmationApiView.as_view(), name='c2b_confirmation_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
