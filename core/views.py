import requests
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# from ipgeolocation.credentials import API_IPSTACK_KEY

from .models import IpData
from .serializer import IpDataSerializer

from ipgeolocation.settings import API_IPSTACK_KEY


def get_ip(request):
    """
    get user ip
    """
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def home(request):
    if request.method == "GET":
        ip = get_ip(request)
        context = {
            "ip": ip,
        }
        return render(request, "geolocation.html", context)


class IpGeolocationList(APIView):
    """
    List all ip geolocation data, create a new one,
    or check geolocation for a specified ip or url by passing ip parameter in url like:
    '/api/ip-geolocation?ip={IP_OR_URL}'
    """
    # html styled form field to run POST on api
    serializer_class = IpDataSerializer

    def get(self, request, *args, **kwargs):
        ip = request.GET.get('ip')
        if ip is not None and ip != '':
            geolocation_data = get_ip_info(ip)
            return Response(geolocation_data)
        else:
            qs = IpData.objects.all()
            serializer = IpDataSerializer(qs, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        if ip geolocation data not found in db
        get data from ipstack about ip and
        save ip geolocation to database
        """

        qs = IpData.objects.all()
        serializer = IpDataSerializer(qs, many=True)

        ip = request.data.get('ip')
        ip_exists = IpData.objects.filter(ip=ip)

        if ip_exists:
            # ip already in db then return all records
            return Response(serializer.data,
                            status=status.HTTP_302_FOUND
                            )
        else:
            # get geolocation of new ip and save it
            geolocation_data = get_ip_info(ip)
            return save_ip_geolocation(geolocation_data)


class IpGeolocationDetails(APIView):
    """
    Retrieve or delete an ip geolocation.
    """
    def get_object(self, ip):
        try:
            return IpData.objects.get(ip=ip)
        except IpData.DoesNotExist:
            raise Http404

    def get(self, request, ip):
        ip = self.get_object(ip)
        serializer = IpDataSerializer(ip)
        return Response(serializer.data)

    def delete(self, request, ip, *args, **kwargs):
        ip = self.get_object(ip)
        ip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def save_ip_geolocation(json_data):
    serializer = IpDataSerializer(data=json_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_ip_info(ip_address):
    """
    collect ip geolocation data using ipstack api
    """
    api_access_key = API_IPSTACK_KEY
    url = 'http://api.ipstack.com/{ip}?access_key={key}'.format(
        ip=ip_address, key=api_access_key
    )

    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers)

    return response.json()
