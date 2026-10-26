from django.views.generic import TemplateView, ListView, DetailView
from .models import ODS

# Vistas provisionales del esqueleto: cada dueño sustituye la suya
# por la ListView o DetailView definitiva (ver 7.3 del kit).
class EnConstruccion(TemplateView):
    template_name = "campus/en_construccion.html"


class PortadaView(EnConstruccion):
    pass


class IniciativaListView(EnConstruccion):
    pass


class IniciativaDetailView(EnConstruccion):
    pass


class ODSListView(ListView):
    model = ODS


class ODSDetailView(DetailView):
    model = ODS


class OrganizacionListView(EnConstruccion):
    pass


class OrganizacionDetailView(EnConstruccion):
    pass