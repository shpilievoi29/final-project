from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from films.models import Film, FilmSession, Hall
from films.serializers import FilmSerializer, FilmSessionSerializer, HallSerializer

"""

Film views for api

"""


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


class HallListAPIView(ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    lookup_url_kwarg = "id"
    lookup_field = "id"
