from django import forms

from ticket.models import Ticket


class TicketForms(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["session", "place"]

