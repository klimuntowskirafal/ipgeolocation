from django.shortcuts import render

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