from rest_framework.test import APITestCase,APIRequestFactory
from users import models as User_models

# Create your tests here.
'''
class AccountBookTest(APITestCase):
    
    def setUp(self) -> None:
        user = User_models.User.objects.create(username="user001",email="test001@test001.com",gender="M",name="user001")
        user.set_password("user001")
        user.save
        self.user=user
    
    def test_create_book(self):
        response = self.client.post(f"account_book/api/{self.user.pk}/")
        self.assertEqual(response.status_code,200)
        self.client.force_login(self.user,)
        response = self.client.post(f"account_book/api/{self.user.pk}/")
'''
    
