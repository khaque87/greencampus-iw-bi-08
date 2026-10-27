from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import ODS, Iniciativa

class ODSTests(TestCase):
    def test_detalle_ods_lista_sus_iniciativas(self):
        ods_clima = ODS.objects.create(numero=13, nombre="Acción por el clima", descripcion="...")
        ods_agua = ODS.objects.create(numero=6, nombre="Agua limpia", descripcion="...")
        
        Iniciativa.objects.create(titulo="Iniciativa Clima", descripcion="...", fecha_inicio=date(2026, 5, 1), ods=ods_clima)
        Iniciativa.objects.create(titulo="Iniciativa Agua", descripcion="...", fecha_inicio=date(2026, 6, 1), ods=ods_agua)
        
        respuesta = self.client.get(reverse("campus:ods_detail", args=[ods_clima.pk]))
        
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Iniciativa Clima")
        self.assertNotContains(respuesta, "Iniciativa Agua")

    def test_ods_sin_iniciativas_muestra_mensaje(self):
        ods_vacio = ODS.objects.create(numero=1, nombre="Fin de la pobreza", descripcion="...")
        
        respuesta = self.client.get(reverse("campus:ods_detail", args=[ods_vacio.pk]))
        
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Este ODS aún no tiene iniciativas.")