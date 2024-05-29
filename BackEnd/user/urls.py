from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet , LoginView , LogoutView , ConfirmEmailView
# Crea un enrutador predeterminado
router = DefaultRouter()

# Registra el viewset con el enrutador
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del enrutador
    path('login/', LoginView.as_view(), name='login'),  # Ruta personalizada para el login
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm/<str:email>/<uuid:token>/', ConfirmEmailView.as_view(), name='confirm-email'),
]

# Obtén las URLs generadas por el enrutador
""" urlpatterns = router.urls """
