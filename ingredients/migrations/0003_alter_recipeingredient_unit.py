# Generated by Django 5.1.5 on 2025-06-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ingredients", "0002_alter_ingredient_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="unit",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
