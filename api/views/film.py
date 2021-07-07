from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from films.models import Film, FilmSession
from films.serializers import FilmSerializer, FilmSessionSerializer


class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    lookup_field = "slug"


class FilmSessionListAPIView(ListCreateAPIView):
    queryset = FilmSession.objects.all()
    serializer_class = FilmSessionSerializer


class FilmSessionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FilmSession.objects.all()
    serializer_class = FilmSessionSerializer
    lookup_url_kwarg = "id"
    lookup_field = "id"
