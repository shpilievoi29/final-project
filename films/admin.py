"""
Implementation admin in films app
"""

from django.contrib import admin

from films.models import Film, Category, FilmSession, Hall


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']
    ordering = ['id']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ['image', 'category', 'film_name', 'film_description', 'slug']
    list_display = ['id', 'image', 'category', 'film_name', 'film_description', 'slug']
    ordering = ['id']
    prepopulated_fields = {'slug': ['film_name', ]}


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    fields = ["hall", "places"]
    list_display = ["hall", "places"]


@admin.register(FilmSession)
class FilmSessionAdmin(admin.ModelAdmin):
    fields = ["film_name", "price", "date_of_beginning", "date_of_ending", "time_start",
              "time_finish", "created_hall"]
    list_display = ["film_name", "price", "date_of_beginning", "date_of_ending", "time_start",
                    "time_finish", "created_hall"]
    ordering = ['id']
