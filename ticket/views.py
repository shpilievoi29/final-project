"""
Implemented Ticket views
"""
from urllib import request

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from ticket.models import Ticket
from user.models import Cash

"""
Creation create view for Ticket

"""


class TicketCreateView(CreateView):
    model = Ticket
    fields = ["session", "place"]
    template_name = "ticket/order.html"

    def form_valid(self, form):
        form.instance.customer = self.request.user
        wallet = Cash.objects.get(username=form.instance.customer).wallet
        total = form.instance.place * form.instance.session.price
        if total > wallet:
            return HttpResponseRedirect(reverse("ticket:create"))

        return super(TicketCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ticket:list")


"""

Creation ticket list View
"""


class TicketListView(ListView):
    http_method_names = ["head", "options", "get"]
    model = Ticket
    template_name = "ticket/order_list.html"

    def get_queryset(self):
        queryset = super(TicketListView, self).get_queryset()

        return queryset.filter(customer=self.request.user)
