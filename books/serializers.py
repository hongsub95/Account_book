from rest_framework import serializers
from . import models as Book_models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_models.Book
        fields = ["pk","title","user","spend_date","spend_cate","money","bio",]
        ordering=['-pk']

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_models.Book
        fields = ["pk","title","user","spend_date","spend_cate","money","bio",]

class BookPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_models.Book
        fields = ["pk","title","user","spend_date","spend_cate","money","bio",]