from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        self.menu_item1 = Menu.objects.create(title="Oreos", price =2.00, inventory = 100)
        self.menu_item2 = Menu.objects.create(title="PikUps", price = 3, inventory= 20)
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)