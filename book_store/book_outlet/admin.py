from django.contrib import admin
from . models import Book

# Register your models here.
# to do more configuration in the DB, we'll add class BookAdmin.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "rating", )
    list_display = ("title", "author", )


admin.site.register(Book, BookAdmin)
