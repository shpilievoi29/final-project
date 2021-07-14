from django import forms

from films.models import FilmSession

"""

Creations session by forms
"""


class AdminSessionsForm(forms.ModelForm):
    model = FilmSession
    fields = "film_name", "price", "date_of_beginning", "date_of_ending", "time_start", \
             "time_finish", "created_hall"
    template = "admin_session"
