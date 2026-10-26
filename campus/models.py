
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ODS(models.Model):
    numero = models.PositiveSmallIntegerField(
        unique=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(17),
        ],
        help_text="Número del ODS (entre 1 y 17).",
    )
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "ODS"
        verbose_name_plural = "ODS"
        ordering = ["numero"]

    def __str__(self):
        return f"ODS {self.numero}: {self.nombre}"


class Organizacion(models.Model):

    class Tipo(models.TextChoices):
        ONG = "ONG", "ONG"
        ADMINISTRACION_PUBLICA = (
            "ADMIN_PUBLICA",
            "Administración pública",
        )
        EMPRESA = "EMPRESA", "Empresa"
        UNIVERSIDAD = "UNIVERSIDAD", "Universidad"
        OTRO = "OTRO", "Otro"

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(
        max_length=20,
        choices=Tipo.choices,
    )
    descripcion = models.TextField()
    web = models.URLField(
        blank=True,
        null=True,
        help_text="Sitio web de la organización (opcional).",
    )

    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Iniciativa(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    ods = models.ForeignKey(
        ODS,
        on_delete=models.PROTECT,
        related_name="iniciativas",
    )

    organizaciones = models.ManyToManyField(
        Organizacion,
        related_name="iniciativas",
        blank=True,
    )

    class Meta:
        verbose_name = "Iniciativa"
        verbose_name_plural = "Iniciativas"
        ordering = ["-fecha_inicio", "titulo"]

    def __str__(self):
        return self.titulo
