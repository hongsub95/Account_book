from django.db import models

# Create your models here.

#가계부 모델
class Book(models.Model):
    class SpendChoice(models.TextChoices):
        Expenditure = "Expenditure", "지출"
        Income = "Income", "수입"
    title = models.CharField(max_length=30,verbose_name="제목")
    spend_cate = models.CharField(max_length=11, blank=True, verbose_name='소비종류',choices=SpendChoice.choices)
    money = models.IntegerField(verbose_name="금액")
    spend_date = models.DateField(verbose_name="소비날짜")
    bio = models.TextField(null=True,blank=True,verbose_name="상세내용")
    user = models.ForeignKey("users.User",on_delete=models.CASCADE,verbose_name="고객")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='등록날짜')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='수정날짜')

# 단축 url
class UrlShortner(models.Model):
    original_url = models.URLField(max_length=256)
    shorten_url = models.URLField(default='')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="생성날짜")