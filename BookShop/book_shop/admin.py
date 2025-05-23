from django.contrib import admin
from .models import Book, PublisherHouse


class BookAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True


class PublisherHouseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True


admin.site.register(Book, BookAdmin)
admin.site.register(PublisherHouse, PublisherHouseAdmin)
# Register your models here.
