from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from . import permissions as Book_permissions
from . import models as Book_models
from . import serializers as Book_serializers


# 사용자용 가계부 (가계부 주인 혹은 관리자만 접근 가능)

#가계부 생성,리스트 View
class SpendCreateListAPIView(generics.ListCreateAPIView):
    
    permission_classes = [Book_permissions.IsBookUserOrAdminUser]
    
    # 가계부 주인의 쿼리 가져오기
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Book_models.Book.objects.filter(user=user_id).all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Book_serializers.BookCreateSerializer
        else:
            return Book_serializers.BookSerializer

#가계부 조회,수정,삭제 view
class SpendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [Book_permissions.IsBookUserOrAdminUser]
    
    def get_queryset(self):
        book_id = self.kwargs["pk"]
        user_id = self.kwargs["user_id"]
        book = Book_models.Book.objects.filter(user=user_id).all()
        return book.filter(pk=book_id)
    
    
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return Book_serializers.BookPatchSerializer
        else:
            return Book_serializers.BookSerializer



# 관리자용 가계부(관리자만 접근 가능)

#admin용 가계부 생성 및 리스트 view
class AdminSpendCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book_models.Book.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Book_serializers.BookCreateSerializer
        else:
            return Book_serializers.BookSerializer

#admin용 가계부 조회,수정,삭제 view
class AdminSpendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book_models.Book.objects.all()
    allowed_method = ("PATCH","DELETE","GET","OPTION")
    
    def get_queryset(self):
        book_id = self.kwargs["pk"]
        book = Book_models.Book.objects.all()
        return book.filter(pk=book_id)
    
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return Book_serializers.BookPatchSerializer
        else:
            return Book_serializers.BookSerializer
