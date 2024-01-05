from django.contrib import admin
from .models import *

admin.site.register(Profile)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date','updated_at','created_at')
    search_fields = ('name',)
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','id','publication_date','author','updated_at','created_at')
    search_fields = ('title',)
    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'updated_at', 'created_at')
    search_fields = ('name',)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower','condition', 'check_out', 'check_in', 'updated_at', 'created_at')
    search_fields = ('book', 'member')

# @admin.register(BookImage)
# class BookImageAdmin(admin.ModelAdmin):
#     list_display = ('book', 'image','updated_at','created_at')
#     search_fields = ('book',)