from django.conf import settings
from django.conf.urls.static import static
from mpesa.views import index, signup
from django.urls import path, re_path
from django.contrib.auth import views

urlpatterns = [
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
