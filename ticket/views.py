from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from ticket.models import Ticket


class TicketCreateView(CreateView):
    model = Ticket
    fields = ["session", "place"]
    template_name = "ticket/order.html"

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(TicketCreateView, self).form_valid(form)


class TicketListView(ListView):
    http_method_names = ["head", "options", "get"]
    model = Ticket
    template_name = "ticket/order_list.html"

    def get_queryset(self):
        queryset = super(TicketListView, self).get_queryset()

        return queryset.filter(customer=self.request.user, is_deleted=False)
