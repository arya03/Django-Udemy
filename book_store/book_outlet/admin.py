from django.contrib import admin

from .models import Address, Author, Book, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  # readonly_fields = ('slug',)  # Prevent slug from being edited
  prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title
  list_filter = ('author', 'rating',)
  list_display = ('title', 'author', 'rating', 'is_bestSelling')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
