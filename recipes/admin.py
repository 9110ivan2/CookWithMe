from django.contrib import admin
from recipes.models import Recipe

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "description",
        "instructions",
        "prep_time",
        "cook_time",
        "servings",
        "created_at",
        "updated_at",
        "slug",
    )


admin.site.register(Recipe, RecipeAdmin)
