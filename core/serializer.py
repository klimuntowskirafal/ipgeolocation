from .models import IpData

from rest_framework import serializers


class IpDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IpData
        fields = (
            'id',
            'ip',
            'city',
            'country_name',
            'region_name',
            'zip',
        )
