from django import forms
from ticket.models import Ticket

"""
Implemented Ticket form for Users

"""


class TicketForms(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["date", "session"]
