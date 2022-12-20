from django.shortcuts import render
from rest_framework import generics
from . import models as Book_models
from . import serializers as Book_serializers
# Create your views here.

class SpendCreateListAPIView(generics.ListCreateAPIView):
    queryset = Book_models.Book.objects.all()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Book_serializers.BookCreateSerializer
        else:
            return Book_serializers.BookSerializer

class SpendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book_models.Book.objects.all()
    allowed_method = ("PATCH","DELETE","GET","OPTION")
    
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return Book_serializers.BookPatchSerializer
        else:
            return Book_serializers.BookSerializer
