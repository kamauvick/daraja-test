from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline

class LNMCallbackUrlApiView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # return super().create(request, *args, **kwargs)
        print(request.data, 'this is the request data.')
