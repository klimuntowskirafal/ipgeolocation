from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from core.views import home, Api

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('api', Api.as_view(), name="api"),
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

]
