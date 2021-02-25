import json
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from ipgeolocation.credentials import API_IPSTACK_KEY


def get_ip(request):
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
    if request.method == "POST":
        ip_or_url = request.POST.get('ip_or_url')
        geolocation_data = get_ip_info(ip_or_url)
        data = json.loads(geolocation_data)
        return JsonResponse(json.loads(geolocation_data))


class Api(APIView):

    def get(self, request, *args, **kwargs):
        test_data = {
            "ip": "134.201.250.155",
            "country_name": "United States",
            "region_name": "California",
            "city": "Los Angeles",
            "zip": 90013,
        }
        return Response(test_data)

    def post(self, request, *args, **kwargs):
        return redirect("/")


def get_ip_info(ip_address):
    api_access_key = API_IPSTACK_KEY
    url = 'http://api.ipstack.com/{ip}?access_key={key}'.format(
        ip=ip_address, key=api_access_key
    )

    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers)

    return response.text
