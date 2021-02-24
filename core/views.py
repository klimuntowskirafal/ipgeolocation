from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


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
    ip = get_ip(request)
    context = {
        "ip": ip,
    }
    return render(request, "geolocation.html", context)


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
