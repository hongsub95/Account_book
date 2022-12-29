from django.urls import reverse
from rest_framework.test import APITestCase,APIRequestFactory
from rest_framework import status
from users import models as User_models


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.register_url = reverse("user-api:register_api")
        self.login_url = reverse("user-api:login_api")
        self.user_data={
            "username":"user1",
            "name":"user1",
            "email":"user1@user1.com",
            "password":"user1",
            "gender":"M"
        }
    def test_register(self):
        self.client.post(self.register_url,data=self.user_data)
    def test_login(self):
        self.access_token=self.client.post(
            self.login_url,{
                "username":self.user_data.get("username"),
                "password":self.user_data.get("password")
            }
        ).data
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        print(self.access_token)
        
        

'''
class RegisterUserTest(APITestCase):
    def test_register(self):
        register_url = reverse("user-api:register_api")
        user_data={
            "username":"testuser3",
            "name":"testuser3",
            "email":"test03@test03.com",
            "password":"testuser3",
            "gender":"M"
        }
        response = self.client.post(register_url,user_data)
        self.assertEqual(response.status_code,200)

class LoginUserTest(APITestCase):
    
    def test_login(self):
        user = User_models.User.objects.create(
            username="testuser3",name="testuser3",email="test03@test03.com",gender="M"
        )
        user.set_password('testuser3')
        user.save()
        self.user = user
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user-api:login_api"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
'''
        



