from django.urls import path
from . import views


app_name = "user-api"

urlpatterns = [
    path('api/register/',views.RegisterAPIView.as_view(),name="register_api"),
    path('api/login/',views.AuthUserAPIView.as_view())
]
