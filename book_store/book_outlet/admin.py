from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  # readonly_fields = ('slug',)  # Prevent slug from being edited
  prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title
  list_filter = ('author', 'rating',)
  list_display = ('title', 'author', 'rating', 'is_bestSelling')

admin.site.register(Book, BookAdmin)
