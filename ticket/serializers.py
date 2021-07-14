"""

Tickets serializer implementation

"""


from rest_framework import serializers

from ticket.models import Ticket

"""

Implemented class Ticket serializer for rest api

"""


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
