from django.views.generic import TemplateView


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


class OrganizacionListView(EnConstruccion):
    pass


class OrganizacionDetailView(EnConstruccion):
    pass
