from django.urls import path
from .views import UploadDataView, get_json, data_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="test case itk data",
        default_version="v1",
        description="api data",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("upload/", UploadDataView.as_view(), name="upload"),
    path("json/", get_json, name="json"),
    path("", data_view, name="index"),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="docs",
    ),
]
