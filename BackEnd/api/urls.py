from django.urls import path, include
from .view.ProductView import ProductViewSet

urlpatterns = [
    # path('auth/register',views.UserRegisterView.as_view(),name="user_register"),#Registrar un usuario
    #path('api/product', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name="product")
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name="product-list"),  # Esta es la ruta para la URL raíz
    path('product/<int:pk>', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="product"),

]
