from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
# Crea un enrutador predeterminado
router = DefaultRouter()

# Registra el viewset con el enrutador
router.register(r'users', UserViewSet, basename='users')

# Obtén las URLs generadas por el enrutador
urlpatterns = router.urls