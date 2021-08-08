from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from info_manager.models import CountryInformation
from info_manager.serializers import CountryInformationSerializer


@api_view(['GET'])
def welcome(request):
    current_site = get_current_site(request).domain
    absurl = 'https://' + current_site + '/api/v1/view/country-info-list'
    return Response('HI, YOU ARE WELCOME! --> Browsable Route: %s' % absurl)


@api_view(['GET',])
def country_info_list(request):
    # See list of all country information
    countries_info = CountryInformation.objects.all()
    serializer = CountryInformationSerializer(countries_info, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def country_details(request):
    # find country-details by country name
    country_name = request.data.get('country_name', '').upper()
    try:
        country_info = CountryInformation.objects.get(country_name=country_name)
        serializer = CountryInformationSerializer(country_info)
        return Response(serializer.data)
    except:
        return Response({'Response': 'Opps! Information Not Found.(Please check your country name)'},
                         status=status.HTTP_204_NO_CONTENT)


@api_view(['POST',])
def create_country_info(request):
    # Create new country info
    country_info = request.data
    serializer = CountryInformationSerializer(data=country_info)

    if serializer.is_valid():
        country_name = request.data.get('country_name').upper()
        if CountryInformation.objects.filter(country_name=country_name).exists():
            return Response({'Response': 'Already Exist!'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_country_info(request):
    # Update country info
    country_name = request.data.get('country_name').upper()
    if CountryInformation.objects.filter(country_name=country_name).exists():
        model = CountryInformation.objects.get(country_name=country_name)
        serializer = CountryInformationSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Response': 'Not Found'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_country_info(request):
    # Delete country info instance
    country_name = request.data.get('country_name').upper()
    if CountryInformation.objects.filter(country_name=country_name).exists():
        country_info = CountryInformation.objects.get(country_name=country_name)
        country_info.delete()
        return Response('Successfully Deleted.')
    else:
        return Response({'Response': 'Opps! Not Found.'}, status=status.HTTP_204_NO_CONTENT)
