from rest_framework import routers

from .view.ProductView import ProductViewSet
from .view.CategoryView import CategoryViewSet
from .view.BrandView import BrandViewSet
from .view.SaleView import SaleViewSet
from .view.SaleDetailView import SaleDetailViewSet

router = routers.DefaultRouter()

router.register('product', ProductViewSet, 'productList')
router.register('category', CategoryViewSet, 'categoryList')
router.register('brand', BrandViewSet, 'brandList')
router.register('sale', SaleViewSet, 'saleList')
router.register('saleDetail', SaleDetailViewSet, 'saleDetailList')


urlpatterns = router.urls