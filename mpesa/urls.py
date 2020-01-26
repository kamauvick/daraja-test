from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path,include
from django.contrib.auth import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
