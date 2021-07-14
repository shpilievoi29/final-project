from django.urls import path

from api.views.ticket import TicketListAPIView, TicketDetailAPIView
"""

Ticket urls for api

"""
app_name = "ticket"

urlpatterns = [
    path('', TicketListAPIView.as_view(), name="list"),
    path('<int:id>/', TicketDetailAPIView.as_view(), name="detail"),
]
