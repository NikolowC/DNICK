from django.contrib import admin
from car_repair.models import Repair, Car, Workshop, Manufacturer, WorkshopManufacturer


class WorkshopManufacturerInline(admin.TabularInline):
    model = WorkshopManufacturer
    extra = 1


class RepairAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        "car_type",
        "speed_limit",
    )


class WorkshopAdmin(admin.ModelAdmin):
    inlines = [WorkshopManufacturerInline]

    def has_change_permission(self, request, obj=None):
        return obj is None

    def has_delete_permission(self, request, obj=None):
        return False


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Repair, RepairAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
