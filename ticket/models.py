from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from films.models import FilmSession


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    session = models.ForeignKey(FilmSession, on_delete=models.CASCADE)
    place = models.PositiveSmallIntegerField(default=1)
    customer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="+"
    )

    def __repr__(self):
        return f"Ticket ('{self.id}')"

    def __str__(self):
        return f"{self.id}|-session: {self.session}|-place: {self.place}|-customer" \
               f" {self.customer}"

    def get_absolute_url(self):
        return reverse_lazy("film:list", kwargs={"pk": self.id})
