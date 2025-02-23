from django.contrib import admin
from categories.models import  Category, RecipeCategory
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('recipe','category')

admin.site.register(RecipeCategory, RecipeCategoryAdmin)
admin.site.register(Category, CategoryAdmin)



