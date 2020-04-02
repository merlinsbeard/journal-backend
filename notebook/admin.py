from django.contrib import admin
from .models import Page, Category, PageCategory, PageMedia, Tag


admin.site.register(Page)
admin.site.register(Category)
admin.site.register(PageCategory)
admin.site.register(PageMedia)
admin.site.register(Tag)
