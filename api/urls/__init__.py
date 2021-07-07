from django.urls import path, include

app_name = "api"

urlpatterns = [

    path("user/", include("api.urls.user", namespace="user"), name="user"),
    path("ticket/", include("api.urls.ticket", namespace="ticket"), name="ticket"),
]