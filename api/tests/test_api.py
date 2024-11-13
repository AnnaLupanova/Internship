from rest_framework.test import APITestCase
from rest_framework import status
from api.models import User, Order


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'name': 'Test',
            'email': 'test@example.com',
            'age': 30
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        self.user_data = {
            'name': 'Test2',
            'email': 'test2@example.com',
            'age': 30
        }
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test2')
        self.assertEqual(response.data['email'], 'test2@example.com')
        self.assertEqual(response.data['age'], 30)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test')

    def test_update_user(self):
        update_data = {
            'name': 'Test Update',
            'email': 'update@example.com',
            'age': 28
        }
        response = self.client.put(f'/api/users/{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Update')
        self.assertEqual(response.data['email'], 'update@example.com')
        self.assertEqual(response.data['age'], 28)


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name="admin", email="admin@example.com", age=30)
        self.order_data = {
            'title': 'Order 1',
            'description': 'This is a description.',
            'user': self.user.id
        }

    def test_create_order(self):
        response = self.client.post('/api/orders/', self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Order 1')
        self.assertEqual(response.data['description'], 'This is a description.')
        self.assertEqual(response.data['user'], self.user.id)

    def test_create_order_without_user(self):
        invalid_order_data = {
            'title': 'Order 2',
            'description': 'Another description.',
            'user': 9999
        }
        response = self.client.post('/api/orders/', invalid_order_data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], "User not found")

    def test_get_orders(self):
        Order.objects.create(title="Order 2", description="Description 2", user=self.user)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_order(self):
        order = Order.objects.create(title="Order 3", description="Description 3", user=self.user)
        update_data = {
            'title': 'Updated Order 3',
            'description': 'Updated description.',
            'user': self.user.id
        }
        response = self.client.put(f'/api/orders/{order.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Order 3')
        self.assertEqual(response.data['description'], 'Updated description.')

    def test_get_single_order(self):
        order = Order.objects.create(title="Order 4", description="Description 4", user=self.user)
        response = self.client.get(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Order 4')
        self.assertEqual(response.data['description'], 'Description 4')