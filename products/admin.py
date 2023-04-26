from django.contrib import admin
from .models import Category, Product, File

from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file', 'file_type', 'is_enable']
    extra = 0


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin]
