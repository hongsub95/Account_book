from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"
    first_name = None
    last_name = None
    name = models.CharField(max_length=100,verbose_name="이름")
    gender = models.CharField(max_length=1, blank=True, verbose_name='성별',choices=GenderChoices.choices)
    birthday = models.DateField(null=True, blank=True, verbose_name="생년월일")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='등록날짜')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='갱신날짜')
