from django.contrib import admin

from films.models import Film, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']
    ordering = ['id']


@admin.register(Film)
class ProductAdmin(admin.ModelAdmin):
    fields = ['image', 'category', 'film_name', 'price', 'film_description', 'slug']
    list_display = ['id', 'image', 'category', 'film_name', 'price', 'film_description', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ['film_name', ]}
