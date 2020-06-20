from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Work, Technology, Image


class ImageInline(admin.TabularInline):
    model = Image


class TechnologyInline(admin.TabularInline):
    model = Technology.work.through


@admin.register(Work)
class WorkAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        TechnologyInline,
        ImageInline
    ]
    ordering = ('order',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    inlines = [
        TechnologyInline
    ]
    exclude = ('work',)
