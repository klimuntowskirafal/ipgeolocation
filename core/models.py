from django.contrib.auth.models import User
from django.db import models


class IpData(models.Model):
    ip = models.CharField(blank=True, null=True, max_length=20)
    country_name = models.CharField(blank=True, null=True, max_length=50)
    region_name = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    zip = models.CharField(blank=True, null=True, max_length=8)
    timestamp = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.ip
