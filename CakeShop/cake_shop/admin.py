from django.contrib import admin
from cake_shop.models import Cake, Baker
from django.db.models import Count


class CakeAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        baker = Baker.objects.filter(user=request.user).first()
        baker_cakes = Cake.objects.filter(baker=baker).all()

        if not change and baker_cakes.count() >= 10:
            return

        sum = 0
        for cake in baker_cakes:
            sum += cake.price

        if not change and sum + obj.price > 10000:
            return

        if Cake.objects.filter(name=obj.name).exists():
            return

        obj.baker = baker
        obj.save()

    def has_change_permission(self, request, obj=None):
        return obj and obj.baker.user == request.user

    def has_view_permission(self, request, obj=None):
        return True


class BakerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        if request.user.is_superuser:
            qs = super(BakerAdmin, self).get_queryset(request)
            return qs.annotate(cakes_count=Count("cakes")).filter(cakes_count__lt=5)
        return qs


admin.site.register(Baker, BakerAdmin)
admin.site.register(Cake, CakeAdmin)
# Register your models here.
