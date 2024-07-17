from django.contrib import admin

from .models import Employee, Store, Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "phone_number"]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "employee"]
    search_fields = ["name"]


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["store", "employee", "timestamp", "latitude", "longitude"]
    search_fields = ["employee__name", "store__name"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
