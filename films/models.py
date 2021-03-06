"""
Implemented Category , Film, Hall, Session models,
"""

from django.urls import reverse_lazy

from django.db import models

"""
Category of films model

"""


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


"""
Film model
"""


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


"""
Hall model for sessions

"""


class Hall(models.Model):
    hall = models.CharField(unique=True, max_length=100, verbose_name="hall")
    places = models.IntegerField(default=50)

    def __str__(self):
        return f"|-Hall: {self.hall}|- Free places:{self.places}"


"""

Films sessions model

"""


class FilmSession(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    film_name = models.ForeignKey(Film, on_delete=models.CASCADE, null=True,
                                  db_column="title")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_beginning = models.DateField(db_column="date start time sessions")
    date_of_ending = models.DateField(db_column="date finish time sessions")
    time_start = models.TimeField(blank=True, db_column="start time sessions")
    time_finish = models.TimeField(blank=True, db_column="finish time sessions")
    created_hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="hall")

    def __repr__(self):
        return f"Session ('{self.id}')"

    def __str__(self):
        return f"|-title: {self.film_name}" \
               f"|-price: {self.price}|-date of beginning:{self.date_of_beginning}| day of " \
               f"ending:{self.date_of_ending}|-start time:{self.time_start}" \
               f"|-finish time:{self.time_finish}|-free places: {self.get_free_places_in_hall()}"

    def get_free_places_in_hall(self):
        from ticket.models import Ticket
        session_tickets = Ticket.objects.filter(session=self.id)
        place_count = 0
        for ticket in session_tickets:
            place_count += ticket.place
        self.created_hall.places -= place_count
        return self.created_hall.places
