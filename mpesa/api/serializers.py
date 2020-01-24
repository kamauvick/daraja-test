from rest_framework import serializers
from mpesa.models import LNMOnline

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = ('id', )
