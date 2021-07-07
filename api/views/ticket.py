"""

Ticket API view implementation

"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ticket.models import Ticket
from ticket.serializers import TicketSerializer


class TicketListAPIView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_url_kwarg = "id"
    lookup_field = "id"
