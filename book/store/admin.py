from django.contrib import admin

# Register your models here.
from store.models import Book, Service, Album


class AlbumInline(admin.TabularInline):
    fk_name = 'book'
    model = Album


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['name', 'year', 'description']
    list_display = ['name', 'year']
    list_filter = ['year', 'name']
    inlines = [AlbumInline, ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description']
