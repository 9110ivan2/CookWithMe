from django.contrib import admin
from ingredients.models import RecipeIngredient, Ingredient

# Register your models here.


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "quantity", "unit")


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
