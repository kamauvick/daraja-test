from django.conf import settings
from django.conf.urls.static import static
from mpesa.views import index, signup
from django.urls import path, re_path
from django.contrib.auth import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
