from django.contrib import admin
from django.urls import path , include

# Requerimientos de static
from django.conf.urls.static import static
from django.conf import settings

# Requerimientos que usa Swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view as swagger_get
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = swagger_get(
   openapi.Info(
      title="Beautica API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #Tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls')),  # Incluir las URLs de api
    path('users/', include('user.urls')),  # Incluir las URLs de users

    # Rutas que se usan para la documentacion
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)