from django.contrib import admin
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'recipe', 'rating', 'created_at')
    search_fields = ('user__username', 'recipe__title', 'nickname')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Review, ReviewAdmin)