from django.test import TestCase
from api.models import User, Order


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="John", email="john@example.com", age=30)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "John")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.age, 30)


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="John", email="john@example.com", age=30)
        self.order = Order.objects.create(title="Order 1", description="Description", user=self.user)

    def test_order_creation(self):
        self.assertEqual(self.order.title, "Order 1")
        self.assertEqual(self.order.description, "Description")
        self.assertEqual(self.order.user, self.user)
