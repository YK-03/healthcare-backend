from django.urls import path

from .views import (
    MappingListCreateView,
    MappingDetailView,
    PatientMappingListView,
)


urlpatterns = [
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),
    path(
        "patient/<int:patient_id>/",
        PatientMappingListView.as_view(),
        name="patient-mappings",
    ),
    path(
        "<int:pk>/",
        MappingDetailView.as_view(),
        name="mapping-detail",
    ),
]