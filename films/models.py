from django.urls import reverse_lazy
from django.utils.text import slugify

from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def __str__(self):
        return self.category

    @property
    def name(self):
        return self.category


class Film(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    film_name = models.CharField(max_length=255, verbose_name="a name title",
                                 help_text="255 characters or fever")
    film_description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='static/media/', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,
                                 db_column='category')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=255, help_text=("letters, hyphens, numbers and"
                                                       " underscores"))

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def __str__(self):
        return self.film_name

    def get_absolute_url(self):
        return reverse_lazy("film:detail", kwargs={"slug": self.slug})

    @property
    def name(self):
        return self.film_name
