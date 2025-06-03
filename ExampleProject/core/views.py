from django.shortcuts import render
from django.views.generic import TemplateView
from vintagestory_masterserver.models import VSServer

# Create your views here.

class ServerListView(TemplateView):
    template_name = "core/server_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vs_servers = VSServer.objects.all()
        num_players = sum((server.players for server in vs_servers))
        num_servers = vs_servers.count()
        context["servers"] = vs_servers
        context["num_players"] = num_players
        context["num_servers"] = num_servers
        return context