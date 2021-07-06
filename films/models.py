"""
Implemented Category , Film, Hall, Session models,
"""

from django.urls import reverse_lazy

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
    image = models.ImageField(upload_to="static/media/", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 db_column='category')
    slug = models.SlugField(max_length=255, help_text=("letters, hyphens, numbers and"
                                                       " underscores"))

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def __str__(self):
        return self.film_name

    def get_absolute_url(self):
        return reverse_lazy("films:detail", kwargs={"slug": self.slug})

    @property
    def name(self):
        return self.film_name


class Hall(models.Model):
    HALL_CHOICES = [
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]

    ]
    hall = models.PositiveSmallIntegerField(choices=HALL_CHOICES, default=5,
                                            verbose_name="hall choices")
    places = models.IntegerField(default=50)

    def __str__(self):
        return f"|-Hall: {self.hall}|- Places:{self.places}"


class FilmSession(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    film_name = models.ForeignKey(Film, on_delete=models.CASCADE, null=True,
                                  db_column="title")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time_start = models.TimeField(blank=True, db_column="start time sessions")
    time_finish = models.TimeField(blank=True, db_column="finish time sessions")
    created_hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="hall")

    def __repr__(self):
        return f"Session ('{self.id}')"

    def __str__(self):
        return f"{self.id}|-title: {self.film_name}" \
               f"|-price: {self.price}|-date{self.date}|-start time:{self.time_start}|-finish time:" \
               f"{self.time_finish}|-hall:{self.created_hall}"
