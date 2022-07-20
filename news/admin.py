from django.contrib import admin
from .models import Category, Tag, Region, News


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagAdmin)


class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Region, RegionAdmin)


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, NewsAdmin)
