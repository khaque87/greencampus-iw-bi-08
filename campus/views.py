from django.views.generic import TemplateView, ListView, DetailView
from .models import ODS, Iniciativa


# Vistas provisionales del esqueleto: cada dueño sustituye la suya
# por la ListView o DetailView definitiva (ver 7.3 del kit).
class EnConstruccion(TemplateView):
    template_name = "campus/en_construccion.html"


class PortadaView(TemplateView):
    template_name = "campus/portada.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destacadas = []
        for ods in ODS.objects.all():
            ultima = Iniciativa.objects.filter(ods=ods).order_by("-fecha_inicio").first()
            if ultima:
                destacadas.append(ultima)
        context["destacadas"] = destacadas
        return context


class IniciativaListView(ListView):
    model = Iniciativa
    template_name = "campus/iniciativa_list.html"
    context_object_name = "iniciativa_list"
    queryset = Iniciativa.objects.select_related("ods")


class IniciativaDetailView(DetailView):
    model = Iniciativa
    template_name = "campus/iniciativa_detail.html"
    context_object_name = "iniciativa"


class ODSListView(EnConstruccion):
    pass


class ODSDetailView(EnConstruccion):
    pass


class OrganizacionListView(EnConstruccion):
    pass


class OrganizacionDetailView(EnConstruccion):
    pass
