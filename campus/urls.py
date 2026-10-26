from django.urls import path

from . import views

app_name = "campus"
urlpatterns = [
    path("", views.PortadaView.as_view(), name="portada"),
    path("iniciativas/", views.IniciativaListView.as_view(), name="iniciativa_list"),
    path("iniciativas/<int:pk>/", views.IniciativaDetailView.as_view(), name="iniciativa_detail"),
    path("ods/", views.ODSListView.as_view(), name="ods_list"),
    path("ods/<int:pk>/", views.ODSDetailView.as_view(), name="ods_detail"),
    path("organizaciones/", views.OrganizacionListView.as_view(), name="organizacion_list"),
    path("organizaciones/<int:pk>/", views.OrganizacionDetailView.as_view(), name="organizacion_detail"),
]
