from django.urls import path
from . import views

app_name ='account-book'

urlpatterns = [
   path('',views.SpendCreateListAPIView.as_view(),name="book_api"),
   path('<int:pk>/',views.SpendRetrieveUpdateDestroyView.as_view(),name="book_api_item")
]
