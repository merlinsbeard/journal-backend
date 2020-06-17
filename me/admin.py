from django.contrib import admin
from .models import Me


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
