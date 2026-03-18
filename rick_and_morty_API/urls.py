from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/characters/", include("characters.urls", namespace="characters")),
    path("api/doc/", SpectacularAPIView.as_view(), name="documentation"),
    # Optional UI:
    path(
        "api/doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="documentation"),
        name="swagger-ui",
    ),
]
