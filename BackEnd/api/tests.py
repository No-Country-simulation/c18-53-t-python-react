from django.test import TestCase
from user.models import User
from api.models import Product, Shopping, ShoppingItem, Brand, Category

class ShoppingTestCase(TestCase):
    def setUp(self):
        # Crear un usuario
        self.user = User.objects.create_user(first_name='cliente2', password='asdasd1231233', email="cliente2@gmail.com")
        
        # Crear una categoría
        self.category = Category.objects.create(name='Electronics', description='Electronics products')
        
        # Crear una marca
        self.brand = Brand.objects.create(name='GenericBrand'""" , description='Generic brand description' """, img='img_brand/generic.jpg')
        
        # Crear productos
        self.product1 = Product.objects.create(name='Celular', price=500, branding=self.brand, category_id=self.category)
        self.product2 = Product.objects.create(name='Televisor', price=1500, branding=self.brand, category_id=self.category)

    def test_create_shopping(self):
        # Crear un pedido
        shopping = Shopping.objects.create(user_name=self.user, product_id=self.product1)
        
        # Agregar artículos al pedido
        item1 = ShoppingItem.objects.create(shopping=shopping, product_id=self.product1, quantity=10)
        item2 = ShoppingItem.objects.create(shopping=shopping, product_id=self.product2, quantity=5)
        
        # Verificar que el pedido y los artículos se han creado correctamente
        self.assertEqual(shopping.user_name, self.user)
        self.assertEqual(ShoppingItem.objects.filter(shopping=shopping).count(), 2)
        self.assertEqual(item1.product_id.name, 'Celular')
        self.assertEqual(item2.quantity, 5)
