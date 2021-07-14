from django.urls import path

from api.views.film import FilmListAPIView, FilmDetailAPIView, FilmSessionListAPIView, \
    FilmSessionDetailAPIView, HallListAPIView, HallDetailAPIView

"""

Film urls for api

"""

app_name = "film"

urlpatterns = [
    path('', FilmListAPIView.as_view(), name="list"),
    path('<slug>/', FilmDetailAPIView.as_view(), name="detail"),
    path('session/', FilmSessionListAPIView.as_view(), name="session_list"),
    path('session/<int:id>/', FilmSessionDetailAPIView.as_view(), name="session_detail"),
    path('hall/', HallListAPIView.as_view(), name="hall_list"),
    path('hall/<int:id>/', HallDetailAPIView.as_view(), name="hall_detail"),

]
