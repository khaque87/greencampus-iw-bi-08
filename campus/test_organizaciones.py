from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import ODS, Iniciativa, Organizacion


class PaginasTests(TestCase):
    def test_todas_las_paginas_responden(self):
        ods = ODS.objects.create(numero=13, nombre="Acción por el clima", descripcion="…")
        organizacion = Organizacion.objects.create(nombre="Deusto Verde", tipo="ONG", descripcion="…")
        iniciativa = Iniciativa.objects.create(titulo="Huerto", descripcion="…",
                                               fecha_inicio=date(2026, 9, 1), ods=ods)
        urls = [
            reverse("campus:portada"),
            reverse("campus:iniciativa_list"),
            reverse("campus:iniciativa_detail", args=[iniciativa.pk]),
            reverse("campus:ods_list"),
            reverse("campus:ods_detail", args=[ods.pk]),
            reverse("campus:organizacion_list"),
            reverse("campus:organizacion_detail", args=[organizacion.pk]),
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)


class OrganizacionTests(TestCase):
    def setUp(self):
        self.ods = ODS.objects.create(numero=4, nombre="Educación de calidad", descripcion="…")
        self.uni = Organizacion.objects.create(nombre="Universidad de Deusto",
                                               tipo="UNIVERSIDAD", descripcion="…")
        self.ong = Organizacion.objects.create(nombre="Deusto Verde", tipo="ONG", descripcion="…")
        self.taller = Iniciativa.objects.create(titulo="Taller de reciclaje", descripcion="…",
                                                fecha_inicio=date(2026, 10, 1), ods=self.ods)
        self.charla = Iniciativa.objects.create(titulo="Charla sobre el agua", descripcion="…",
                                                fecha_inicio=date(2026, 10, 15), ods=self.ods)
        self.taller.organizaciones.add(self.uni)
        self.charla.organizaciones.add(self.ong)

    def test_detalle_organizacion_lista_sus_iniciativas(self):
        respuesta = self.client.get(reverse("campus:organizacion_detail", args=[self.uni.pk]))
        self.assertContains(respuesta, "Taller de reciclaje")
        self.assertNotContains(respuesta, "Charla sobre el agua")

    def test_lista_muestra_el_tipo_con_su_nombre(self):
        respuesta = self.client.get(reverse("campus:organizacion_list"))
        self.assertContains(respuesta, "Universidad de Deusto")
        self.assertContains(respuesta, "<p>Universidad</p>", html=True)
        self.assertNotContains(respuesta, "UNIVERSIDAD")

    def test_detalle_inexistente_da_404(self):
        respuesta = self.client.get(reverse("campus:organizacion_detail", args=[9999]))
        self.assertEqual(respuesta.status_code, 404)
