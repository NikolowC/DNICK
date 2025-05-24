from django.contrib import admin
from food_shop.models import FoodProduct, Category, Sale, Client, SoldProduct


class SoldProductInline(admin.TabularInline):
    model = SoldProduct
    extra = 1


class FoodProductAdmin(admin.ModelAdmin):
    inlines = [SoldProductInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
    )


class SaleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodProduct, FoodProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale, SaleAdmin)


# Register your models here.
