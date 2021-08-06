from rest_framework import serializers
from info_manager.models import CountryInformation


class CountryInformationSerializer(serializers.HyperlinkedModelSerializer):
    """ JSON representation of Country Information """
    class Meta:
        model = CountryInformation
        fields = ['country_name', 'country_code', 'iso_code', 'population', 'area', 'flag']
