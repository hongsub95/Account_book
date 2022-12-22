from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class RegisterUserTest(APITestCase):
    def test_register(self):
        url = reverse('user/api/register')
        user_data = {
            "username":"user01",
            "password":"user01",
            "email":"test01@test01.com",
            "gender":"M",
            "name":"user01"
        }
        response = self.client.post(url,user_data)
        print(self.assertEqual(response.status,200))



