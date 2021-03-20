from django.contrib import admin

from store.models import Book, Journal
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields =['num_pages']

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    search_fields = ['publisher']