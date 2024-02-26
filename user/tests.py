from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from .models import User 


class LoginTest(APITestCase):
    def setUp(self):
        self.credentials = {'phone':'09026386221','email':'test@gmail.com','password':'test123'}
        self.client = APIClient()
        self.login_url = reverse('LOGIN')
        self.register_url = reverse('REGISTER')
        self.user = User.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(self.login_url, {'phone': '09026386221', 'password': 'test123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('tokens', response.json())

    def test_login_failure_phone(self):
        response = self.client.post(self.login_url, {'phone': '09123456789', 'password': 'test123'})
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('tokens', response.json())
    
    def test_login_failure_password(self):
        response = self.client.post(self.login_url, {'phone': '09026386221', 'password': 'wrong'})
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('tokens', response.json())

    def test_register_success(self):
        response = self.client.post(self.register_url, self.credentials)
        self.assertEqual(response.status_code, 201)
        # self.assertIn('tokens', response.json())
