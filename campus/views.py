from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import render, redirect
from .forms import IniciativaForm
from .models import ODS, Iniciativa, Organizacion


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
            ultima = ods.iniciativas.order_by("-fecha_inicio").first()
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


class ODSListView(ListView):
    model = ODS


class ODSDetailView(DetailView):
    model = ODS


class OrganizacionListView(ListView):
    model = Organizacion


class OrganizacionDetailView(DetailView):
    model = Organizacion


def crear_iniciativa(request):
    if request.method == "POST":
        form = IniciativaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("campus:iniciativa_creada")

    else:
        form = IniciativaForm()

    return render(request, "campus/crear_iniciativa.html", {
        "form": form
    })


def iniciativa_creada(request):
    return render(request, "campus/iniciativa_creada.html")