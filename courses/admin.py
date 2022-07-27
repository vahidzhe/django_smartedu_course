from django.contrib import admin
from . models import Course,Category,Tags

# Register your models here.
@admin.register(Course)
class CourceAdmin(admin.ModelAdmin):
    list_display = ['name','available']
    list_filter = ['available']
    search_fields = ['name','description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} 