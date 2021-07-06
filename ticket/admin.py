from django.contrib import admin

from ticket.models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    fields = ["id", "session", "place"]
    list_display = ["id", "session", "place"]
    ordering = ["id"]


