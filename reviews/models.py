from django.db import models

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
        ordering = ['-created_at']

    def __str__(self):
        reviewer = self.user.username if self.user else self.nickname
        return f"{reviewer} reviewed {self.recipe.title} with rating {self.rating}"