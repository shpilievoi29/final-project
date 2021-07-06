"""
Implemented Film's urls
"""


from django.urls import path

from films.views import FilmListView, FilmDetailView, SessionListView
# AddToCartView,\
#     PurchaseView, ReviewCreateView,

app_name = "film"
urlpatterns = [
    path("", FilmListView.as_view(), name="list"),
    path("film/<slug:slug>/", FilmDetailView.as_view(), name="detail"),
    path("sessions/", SessionListView.as_view(), name="sessions"),
#     path("review/", ReviewCreateView.as_view(), name="review"),
#     path("add-to-cart/<slug:slug>/", AddToCartView.as_view(), name="add-to-cart"),
#     path("purchase/", PurchaseView.as_view(), name="purchase"),
]