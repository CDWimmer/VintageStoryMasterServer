from django.urls import path

from vintagestory_masterserver import views as vs_views
from . import views


urlpatterns = [
    path('list/', views.ServerListView.as_view(), name="server_list"),
    path('prune/', vs_views.VSMasterPruneDB.as_view(), name="prune_vs_servers"),
]