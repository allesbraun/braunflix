from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from braunflix.views import ProgramViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Braunflix",
      default_version='v1',
      description="Local provider of tv shows and movies developed by allesbraun throughout the course of Django Rest offered by Alura",
      terms_of_service="#",
      contact=openapi.Contact(email="allesbraun123@gmail.com"),
      license=openapi.License(name="Apache License 2.0"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('programs', ProgramViewSet, basename='programs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
