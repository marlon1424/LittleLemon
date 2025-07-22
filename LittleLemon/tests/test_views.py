from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Snack Box", price=21, inventory=100)
    
    def test_getall(self):
        pass