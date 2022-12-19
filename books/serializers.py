from rest_framework import serializers
from . import models as Book_models

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_models.Book
        fields = ["name","user","spend_date","spend_cate","money","bio",]