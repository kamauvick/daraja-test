from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from .views import LNMCallbackUrlApiView, C2BConfirmationApiView, C2BValidationApiView, MakeLNMPayment, MakeC2BPayment
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('LNMPayment', MakeLNMPayment)
router.register('C2BPayment', MakeC2BPayment)


urlpatterns = [
    path('lnm/', LNMCallbackUrlApiView.as_view(), name='lnm_callback_url'),
    path('validation_url/', C2BValidationApiView.as_view(), name='c2b_validation_url'),
    path('confirmation_url/', C2BConfirmationApiView.as_view(), name='c2b_confirmation_url'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
