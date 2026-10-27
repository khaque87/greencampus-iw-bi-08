from django.test import TestCase
from datetime import date
from django.urls import reverse
from .models import ODS, Iniciativa, Organizacion

# Create your tests here.


class IniciativaYPortadaTests(TestCase):
    def setUp(self):
        self.ods_clima = ODS.objects.create(
            numero=13, 
            nombre="Acción por el clima", 
            descripcion="Descripción Clima"
        )
        self.org_univ = Organizacion.objects.create(
            nombre="Universidad de Deusto", 
            tipo="UNIVERSIDAD", 
            descripcion="Universidad"
        )

    def test_detalle_inexistente_da_404(self):
        respuesta = self.client.get(reverse("campus:iniciativa_detail", args=[9999]))
        self.assertEqual(respuesta.status_code, 404)

    def test_portada_muestra_la_mas_reciente_de_cada_ods(self):
        antigua = Iniciativa.objects.create(
            titulo="Antigua", 
            descripcion="...", 
            fecha_inicio=date(2024, 3, 1), 
            ods=self.ods_clima
        )
        nueva = Iniciativa.objects.create(
            titulo="Nueva", 
            descripcion="...", 
            fecha_inicio=date(2026, 9, 1), 
            ods=self.ods_clima
        )
        respuesta = self.client.get(reverse("campus:portada"))
        self.assertEqual(respuesta.context["destacadas"], [nueva])

    def test_detalle_iniciativa_muestra_ods_y_organizaciones(self):
        iniciativa = Iniciativa.objects.create(
            titulo="Reciclaje Campus", 
            descripcion="...", 
            fecha_inicio=date(2026, 1, 1), 
            ods=self.ods_clima
        )
        iniciativa.organizaciones.add(self.org_univ)
        
        respuesta = self.client.get(reverse("campus:iniciativa_detail", args=[iniciativa.pk]))
        self.assertContains(respuesta, "Acción por el clima")
        self.assertContains(respuesta, "Universidad de Deusto")
