from django.test import TestCase

from ticket.models import Ticket

"""

Test for app "Ticket"

"""


class TicketModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ticket = Ticket.objects.get(

            id=1,
            session_id=1,
            place=50,
            customer_id=2

        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.ticket.id, int)
        self.assertIsInstance(self.ticket.session_id, int)
        self.assertIsInstance(self.ticket.place, int)
        self.assertIsInstance(self.ticket.customer_id, int)
