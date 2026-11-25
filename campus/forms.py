
from django import forms
from .models import Iniciativa


class IniciativaForm(forms.ModelForm):

    class Meta:
        model = Iniciativa
        fields = [
            "titulo",
            "descripcion",
            "fecha_inicio",
            "ods",
            "organizaciones",
        ]

        widgets = {
           "fecha_inicio": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }
