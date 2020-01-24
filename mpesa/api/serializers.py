from rest_framework import serializers
from mpesa.models import LNMOnline

class LNMOnlineSerializer(serializers.ModelSerializer):
    model = LNMOnline
    fields = ('id', )
