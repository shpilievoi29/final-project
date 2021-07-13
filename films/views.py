"""

Implementations  films views  to display list of films , film detail , sessions of films

"""
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, RedirectView

from films.models import Film, Category, FilmSession

"""

Implemented Film list view

"""


class FilmListView(ListView):
    model = Film
    http_method_names = ["get", "head", "options", "trace"]
    template_name = "film/film.html"

    def get_queryset(self):
        queryset = super(FilmListView, self).get_queryset()
        category_id = self.request.GET.get("category_id")
        if category_id is not None:
            queryset.filter(category_id=category_id)
        return queryset.exclude(id=0)

    def get_context_data(self, *args, **kwargs):
        context = super(FilmListView, self).get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


"""

implemented detail view for films
"""


class FilmDetailView(DetailView):
    model = Film
    template_name = "film/film_detail.html"
    slug_field = "slug"


"""

Sessions list view for sessions 

"""


class SessionListView(ListView):
    model = FilmSession
    http_method_names = ["get", "head", "options", "trace"]
    template_name = "film/sessions.html"
    queryset = FilmSession.objects.all()


class AdminCreateSessionView(CreateView):
    model = FilmSession
    fields = "__all__"
    template_name = "film/admin_session.html"

    def get_success_url(self):
        return reverse_lazy("film:list")
