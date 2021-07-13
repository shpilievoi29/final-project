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
        return f"{self.id}|-session: {self.session}|-bought place(s): {self.place}|-customer" \
               f" {self.customer}"

    @property
    def get_absolute_url(self):
        return reverse_lazy("ticket:list")

    def get_total(self):
        total = self.session.price * self.place
        return total

    def save(self, *args, **kwargs):
        self.customer.cash.wallet -= self.get_total()
        self.customer.cash.save()
        self.total = self.get_total()

        super(Ticket, self).save(*args, **kwargs)

