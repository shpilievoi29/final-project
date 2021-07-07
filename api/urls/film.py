from django.urls import path

from api.views.film import FilmListAPIView, FilmDetailAPIView, FilmSessionListAPIView,\
    FilmSessionDetailAPIView

app_name = "film"

urlpatterns = [
    path('', FilmListAPIView.as_view(), name="list"),
    path('<slug>/', FilmDetailAPIView.as_view(), name="detail"),
    path('session/', FilmSessionListAPIView.as_view(), name="session_list"),
    path('session/<int:id>/', FilmSessionDetailAPIView.as_view(), name="session_detail"),

]