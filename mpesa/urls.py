from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path,include
from django.contrib.auth import views
from rest_framework.routers import DefaultRouter
from .views import MakeLNMPayment, MakeC2BPayment

router = DefaultRouter()
router.register('LNMPayment', MakeLNMPayment)
router.register('C2BPayment', MakeC2BPayment)


urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
