from rest_framework.test import APITestCase,APIRequestFactory
from rest_framework import status
from django.urls import reverse
from users import models as User_models
from . import models as Book_models

# Create your tests here.

class AccountCreateBookTest(APITestCase):
    def setUp(self) -> None:
        user = User_models.User.objects.create(username="user001",email="test001@test001.com",gender="M",name="user001")
        user.set_password("user001")
        user.save
        self.user=user
        self.book =Book_models.Book.objects.create(title="Test1",spend_cate="Expenditure",money="20000",spend_date="2022-12-30",bio="Test1",user=self.user)
    
    def test_create_book(self):
        user_id = self.user.pk
        book_data = {
            "title":"Test0",
            "spend_cate":"Expenditure",
            "money":"30000",
            "spend_date":"2022-12-30",
            "bio":"코딩 하기 위해 삼",
            "user":f"{user_id}"
        }
        response = self.client.post(f"http://127.0.0.1:8000/account_book/api/{user_id}/",data=book_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_patch_book(self):
        user_id = self.user.pk
        book_id = self.book.pk
        book_data = {
            "title":"Test2",
            "spend_cate":"Expenditure",
            "money":"40000",
            "spend_date":"2022-12-30",
            "bio":"Test2",
            "user":f"{user_id}"
        }
        response = self.client.patch(f"http://127.0.0.1:8000/account_book/api/{user_id}/{book_id}/",data=book_data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_delete_book(self):
        user_id = self.user.pk
        book_id = self.book.pk
        response = self.client.delete(f"http://127.0.0.1:8000/account_book/api/{user_id}/{book_id}/")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)