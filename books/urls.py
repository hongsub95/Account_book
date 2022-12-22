from django.urls import path
from . import views

app_name ='account-book'

urlpatterns = [
   path('api/<int:user_id>/',views.SpendCreateListAPIView.as_view(),name="book_api"),
   path('api/<int:user_id>/<int:pk>/',views.SpendRetrieveUpdateDestroyView.as_view(),name="book_api_item"),
   path('admin/api/',views.AdminSpendCreateListAPIView.as_view(),name="admin_book_api"),
   path('admin/api/<int:pk>/',views.AdminSpendRetrieveUpdateDestroyView.as_view(),name="admin_book_api_item"),
   path('api/shorten_url/',views.url_shortner),
   path('api/<new_url>/',views.redirect_url)
]
