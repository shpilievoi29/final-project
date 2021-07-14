from django.urls import path

from ticket.views import TicketCreateView, TicketListView


"""

Implemented URLS for Ticket app


"""

app_name = "ticket"
urlpatterns = [
    path("ticket/", TicketCreateView.as_view(), name="create"),
    path("order/", TicketListView.as_view(), name="list"),

]
