from django.views.generic import DetailView, ListView, TemplateView

from .models import ODS, Iniciativa, Organizacion


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


class ODSListView(EnConstruccion):
    pass


class ODSDetailView(EnConstruccion):
    pass


class OrganizacionListView(ListView):
    model = Organizacion


class OrganizacionDetailView(DetailView):
    model = Organizacion
