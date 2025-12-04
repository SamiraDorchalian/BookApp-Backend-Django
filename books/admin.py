from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'pages', 'datetime_created')
    list_filter = ('year', 'language', 'country')
    search_fields = ('title', 'author', 'country')
    ordering = ('-datetime_created',)

    readonly_fields = ('show_cover',)

    def show_cover(self, obj):
        if obj.cover:
            return format_html(f'<img src="{obj.cover.url}" width="150" height="200" />')
        return "No Image"
    show_cover.short_description = "Cover Preview"