from rest_framework import serializers
from api.models import Api

class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Api
        fields="__all__"