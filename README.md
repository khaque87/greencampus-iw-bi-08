# Green Campus - Grupo IW-BI-08

## Descripción del Proyecto

Green Campus es una aplicación web desarrollada en Django orientada a visibilizar las iniciativas de sostenibilidad de la universidad. Cada iniciativa se clasifica según un Objetivo de Desarrollo Sostenible (ODS) principal y está promovida por una o varias organizaciones, lo que permite consultar la información de forma estructurada tanto por objetivo como por entidad promotora.

## Instalación y Despliegue Local (Entorno Windows)

Para ejecutar este proyecto en un entorno local con los datos de prueba, sigue estos pasos desde la consola:

**1. Clonar el repositorio:**

```bash
git clone https://github.com/khaque87/greencampus-iw-bi-08.git
cd greencampus-iw-bi-08
```

**2. Crear y activar el entorno virtual:**

```bash
mkvirtualenv greencampus
workon greencampus
```

**3. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

**4. Aplicar migraciones de la base de datos:**

```bash
python manage.py migrate
```

**5. Cargar el juego de ensayo (datos de prueba):**

```bash
python -X utf8 manage.py loaddata datos.json
```

**6. Crear el usuario administrador (Superuser):**

```bash
python manage.py createsuperuser
```


**7. Ejecutar el servidor local:**

```bash
python manage.py runserver
```

## Acceso al Panel de Administración (Admin)

- **Ruta:** http://127.0.0.1:8000/admin/
- **Usuario:** `admin`
- **Contraseña:** `admin`

## Reparto de Tareas y Registro de uso de IA

A continuación se detalla el trabajo técnico realizado por cada integrante y la declaración obligatoria del uso de herramientas de Inteligencia Artificial, cumpliendo con la normativa de la entrega.

### Tareas T1.2 y T1.3 - Modelos, Admin y Datos (Rol I2: Luis)

Implementación Técnica:

Luis desarrolló los modelos de datos en `models.py` correspondientes a las entidades ODS, Organización e Iniciativa, estableciendo las relaciones entre ellas mediante claves foráneas (`ForeignKey` con `on_delete=PROTECT`) y relaciones muchos a muchos (`ManyToManyField`). Asimismo, registró las tres entidades en `admin.py` para su gestión desde el panel de administración y generó el archivo `datos.json` mediante el comando `dumpdata`, que constituye el juego de ensayo del proyecto.

Registro de uso de IA:

El código de los modelos y de las migraciones se elaboró manualmente a partir de los apuntes de la asignatura. La IA se utilizó únicamente de forma puntual para generar descripciones y nombres ficticios con los que rellenar rápidamente las iniciativas del juego de ensayo. También código para probar o para perfeccionar cosas.

### Tarea T1.4 - Plantilla Base y CSS (Rol I5: Igor)

Implementación Técnica:

Igor desarrolló el diseño base de la aplicación mediante una estructura de herencia de plantillas de tres niveles, apoyada en `base.html` y `seccion.html`. Programó el archivo `estilos.css` desde cero utilizando CSS propio, sin recurrir a frameworks, y el resultado superó la validación W3C sin errores.

Registro de uso de IA:

Toda la semántica HTML5 y las reglas de CSS se escribieron manualmente. La IA se utilizó únicamente como asistente para buscar combinaciones de colores que cumplieran los estándares de contraste y accesibilidad.

### Tareas T1.5 y T1.6 - Portada e Iniciativas (Rol I3: Erik)

Implementación Técnica:

Erik implementó las vistas `PortadaView`, `IniciativaListView` e `IniciativaDetailView`. En la portada programó la lógica del método `get_context_data` para filtrar y mostrar exclusivamente la iniciativa más reciente de cada ODS.

Registro de uso de IA:

Las vistas y las plantillas se programaron manualmente. La IA se empleó únicamente como consulta rápida para recordar la sintaxis exacta del ORM de Django al ordenar por fecha (`order_by("-fecha_inicio")`).

### Tarea T1.7 - Objetivos de Desarrollo Sostenible (Rol I4: Ander Lizarazu)

Implementación Técnica:

Vistas (views.py): Integración de ListView y DetailView genéricas de Django para conectar los modelos de los ODS con el frontend, renderizando el listado general y el detalle de iniciativas asociadas a cada objetivo.

Plantillas HTML5: Desarrollo de ods_list.html y ods_detail.html. La estructura semántica principal (etiquetas <main> y <section>) se hereda directamente de las plantillas base desarrolladas por Igor. En estos archivos se ha configurado la sintaxis de plantillas de Django ({% for %}, {% empty %}) para iterar dinámicamente la información.

Validación W3C: El código HTML renderizado ha superado el Nu Html Checker sin errores ni advertencias, verificando también el correcto contraste y jerarquía de encabezados.

Registro de uso de IA:

Trabajo Manual: La lógica de las vistas, la herencia de las plantillas y la validación manual de accesibilidad se han realizado de forma íntegra basándome en los apuntes de la asignatura.

Asistencia IA (Apoyo puntual): Utilicé la IA como diccionario técnico para confirmar la sintaxis exacta de importación de las vistas genéricas en Python y consultar los comandos de seguridad para realizar un Update from main en GitHub Desktop sin sobrescribir código ajeno.

### Tarea T1.8 - Organizaciones y Coordinación (Rol I1: Kazi)

Implementación Técnica:

Kazi se encargó de la sección de organizaciones (vistas `OrganizacionListView` y `OrganizacionDetailView`, con sus plantillas y pruebas), de la coordinación del repositorio y de la integración de las ramas en `main`, así como de la configuración base del proyecto (`settings.py` y `urls.py`).

Registro de uso de IA:

He utilizado Claude (Anthropic) como asistente en tres ámbitos:

- **Planificación y estructura inicial:** elaboró el plan de trabajo y el reparto de tareas, y generó el esqueleto inicial de la aplicación.
- **Desarrollo:** generó el código de la sección de organizaciones.
- **Revisión e integración:** me ayudó a revisar las contribuciones del grupo y a resolver conflictos entre ramas.

Por mi parte, coordiné el reparto de tareas, creé el repositorio, ejecuté el proyecto y las pruebas en local y gestioné la integración en `main`.
