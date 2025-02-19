from django.contrib import admin

from blogs.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "header",
        "content",
    )
    list_filter = ("header",)
    search_fields = ("header",)
