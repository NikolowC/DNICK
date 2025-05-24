from django.contrib import admin
from hot_ballon.models import *


class FlightAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


class HotBallonAdmin(admin.ModelAdmin):
    pass


class PilotAirlineInline(admin.TabularInline):
    model = PilotAirline
    extra = 1


class PilotAdmin(admin.ModelAdmin):
    inlines = [PilotAirlineInline]
    list_display = ("firstname", "lastname")


class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name",)


# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(HotBallon, HotBallonAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)
