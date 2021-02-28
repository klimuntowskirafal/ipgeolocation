from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import home, IpGeolocationList, IpGeolocationDetails


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/ip-geolocation',
         IpGeolocationList.as_view(),
         name="ip-geolocation",
         ),
    path('api/ip-geolocation/<ip>',
         IpGeolocationDetails.as_view(),
         ),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
