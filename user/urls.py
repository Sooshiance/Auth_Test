from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from .views import *


urlpatterns = [
    path('', HomeAPIView.as_view(), name='HOME'),
    path('login/', UserLoginAPIView.as_view(), name='LOGIN'),
    path('register/', UserRegisterationAPIView.as_view(), name='REGISTER'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='TOKEN_REFERSH'),
]
