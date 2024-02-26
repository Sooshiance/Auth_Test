from django.urls import reverse_lazy

from rest_framework.test import APITestCase, APIClient

from .models import User 


class LoginTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse_lazy('login')
        self.user = User.objects.create_user(phone='09026386221', email='test@gmail.com', password='test123')

    def test_login_success(self):
        response = self.client.post(self.url, {'phone':'09026386221','password':'test123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_login_failure(self):
        response = self.client.post(self.url, {'phone': '09123456789', 'password': 'wrong'})
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('token', response.data)
