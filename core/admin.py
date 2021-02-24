from django.contrib import admin
from core.models import IpData


# Register your models here.
class IpDataAdmin(admin.ModelAdmin):
    list_display = [
        'ip',
        'country_name',
        'city',
        'timestamp',
    ]

    list_filter = [
        'country_name',
        'city',
        'timestamp',
    ]


admin.site.register(IpData, IpDataAdmin)
