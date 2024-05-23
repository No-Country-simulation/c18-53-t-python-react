from django.urls import path, include
from .view.ProductView import ProductViewSet
from .view.CategoryView import CategoryViewSet
from .view.BrandView import BrandViewSet

urlpatterns = [
    # path('auth/register',views.UserRegisterView.as_view(),name="user_register"),#Registrar un usuario
    #path('api/product', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name="product")
    path('product', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name="product-list"),  
    path('product/<int:pk>', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="product"),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='category'),

    path('brand/', BrandViewSet.as_view({'get': 'list', 'post': 'create'}), name='brand-list'),
    path('brand/<int:pk>', BrandViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='brand'),

]
