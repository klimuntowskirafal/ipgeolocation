from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import home, IpGeolocationList, IpGeolocationDetails

from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('api/ip-geolocation',
         IpGeolocationList.as_view(),
         name="ip-geolocation",
         ),
    path('api/ip-geolocation/<ip>',
         IpGeolocationDetails.as_view(),
         ),
    path(
        r"login/",
        auth_views.LoginView.as_view(
            template_name="login.html", redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        r"logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
